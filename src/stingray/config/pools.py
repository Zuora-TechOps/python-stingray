from stingray.apiclient import Client, StingrayAPIClientError


class Pools(Client):
    """
    Class for interacting with Pools via the REST API
    """
    def __init__(self, host=None, port=None, user=None, password=None,
                 api_version=None, ssl_verify=None):
        super(Pools, self).__init__(host, port, user, password,
                                    api_version, ssl_verify)
        self.config_path = '{0}/config/active/pools/'.format(self.api_version)
        self.pools = {}
        pools_list = self._api_get(self.config_path)
        for pool in pools_list['children']:
            self.pools[pool['name']] = pool['href']

    def get(self, pool):
        """
        Get a Pool object for the request pool.

        Arguments:
            pool (str): The name of the pool to get

        Returns:
            (Pool): The requested pool
        """
        try:
            pool_properties = self._api_get(self.pools[pool])
            return Pool(pool, self.pools[pool], pool_properties['properties'],
                        self.api_host, self.api_port, self.api_user,
                        self.api_password, self.api_version, self.ssl_verify)
        except KeyError:
            raise StingrayAPIClientError(
                "Pool {0} not found".format(pool)
            )

    def add(self, pool, nodes=None, **pool_props):
        """
        Add a new load balancer pool

        Arguments:
            pool (str): The name of the pool to add
            nodes (list): List of nodes for the pool
            pool_props: Additional arguments to set properties of the pool
                        at time of creation.

        Returns:
            (Pool): The new pool
        """
        # Don't create empty pools
        if nodes is None:
            raise StingrayAPIClientError(
                "No nodes specified, cannot create pool"
            )

        if nodes and type(nodes) != list:
            raise StingrayAPIClientError(
                "Nodes must be specified as a list"
            )

        pool_data = dict(
            properties=dict(
                basic=dict(
                    nodes_table=[]
                )
            )
        )

        for prop in pool_props:
            pool_data['properties'].update(prop)

        for node in nodes:
            pool_data['properties']['basic']['nodes_table'].append(dict(
                node=node,
                state='active'
            ))

        add_pool_response = self._api_put(
            '{0}{1}'.format(self.config_path, pool),
            pool_data
        )

        return Pool(pool, '{0}/{1}'.format(self.config_path, pool),
                    add_pool_response['properties'], self.api_host,
                    self.api_port, self.api_user, self.api_password,
                    self.api_version, self.ssl_verify)

    def delete(self, pool):
        """
        Delete a load balancer pool

        Arguments:
            pool (str): The name of the pool to delete

        Returns:
            (dict): Response from the _api_delete method
        """
        return self._api_delete('{0}{1}'.format(self.config_path, pool))


class Pool(Client):
    """
    Class for interacting with individual pools via the REST API
    """
    def __init__(self, pool_name, pool_path, pool_properties, host=None,
                 port=None, user=None, password=None, api_version=None,
                 ssl_verify=None):
        super(Pool, self).__init__(host, port, user, password,
                                   api_version, ssl_verify)
        self.config_path = pool_path
        self.name = pool_name
        self.properties = pool_properties
        self.nodes = dict()

        # API versions 1.0 and 2.0 use a different structure for the pool
        # properties to denote active, draining, and disabled nodes.
        if self.api_version in ['1.0', '2.0']:
            for n in self.properties['basic']['nodes']:
                self.nodes[n] = dict(node=n, state='active')
            for n in self.properties['basic']['draining']:
                self.nodes[n] = dict(node=n, state='draining')
            for n in self.properties['basic']['disabled']:
                self.nodes[n] = dict(node=n, state='disabled')
        else:
            for n in self.properties['basic']['nodes_table']:
                self.nodes[n['node']] = n

        self.status_api = self.get_status()

    def _bad_node(self, node):
        raise StingrayAPIClientError(
            "Node {0} is not a member of this pool".format(node)
        )

    def _update(self):
        """
        Update the properties for the pool on the load balancer
        """
        updated = self._api_put(self.config_path, self.properties)
        self.properties = updated['properties']

    def nodes_status(self):
        """
        Get status info for the nodes in the pool. Some info is found in the
        node properties, some in the node statistics.

        Returns:
            (dict): Nodes and their status, e.g.:
                    {
                      u'10.0.0.1': {
                        'connections': 0,
                        'health': u'alive',
                        'requests': 0,
                        'state': 'active'
                      }
                    }
        """
        node_status = dict()
        for node, node_values in self.nodes.iteritems():
            node_status[node] = dict(
                state=node_values['state'],
            )
            if node_values['state'] in ['active', 'draining'] and self.api_version != "1.0":
                stats = self.status_api.statistic('nodes', 'node', node)
                node_status[node]['health'] = stats['state']
                node_status[node]['connections'] = stats['current_conn']
                node_status[node]['requests'] = stats['current_requests']

        return node_status

    def add_node(self, node, state='active', priority=1, weight=1):
        """
        Add a new node to the pool

        Arguments:
            node (str): The node to add. Must be in accepted pool node config
                        format: <ip or dns name>:<port>
            state (str): active, draining, or disabled. Default is active
                         because it should be pretty rare to add a node in
                         any other state.
            priority (int): Load balancer priority for the node
            weight (int): Load balancer weight for the node

        Returns:
            (dict): Pool nodes status
        """
        # Deal with the properties differences for versions 1.0 and 2.0
        if self.api_version in ['1.0', '2.0']:
            if state == "draining":
                self.properties['basic']['draining'].append(node)
            elif state == "disabled":
                self.properties['basic']['disabled'].append(node)
            else:
                self.properties['basic']['nodes'].append(node)
            self.properties['load_balancing']['node_weighting'].append(dict(node=node, weight=weight))
            self.nodes[node] = dict(node=node, state=state)
        else:
            self.properties['basic']['nodes_table'].append(dict(
                node=node,
                state=state,
                priority=priority,
                weight=weight,
            ))
            self.nodes[node] = self.properties['basic']['nodes_table'][-1]

        # Update the pool on the load balancer with the new properties
        self._update()

        return self.nodes_status()

    def drain_node(self, node):
        """
        Set a node in the pool to draining status

        Arguments:
            node (str): The node to drain

        Returns:
            (dict): Pool nodes status
        """
        # Make sure the node is in the pool
        drain_node = self.nodes.get(node, None)
        if drain_node is None:
            self._bad_node(node)

        drain_node['state'] = 'draining'

        # Deal with the properties differences for versions 1.0 and 2.0
        if self.api_version in ['1.0', '2.0']:
            self.properties['basic']['draining'].append(node)
            if drain_node['state'] == "disabled":
                self.properties['basic']['disabled'].pop(self.properties['basic']['disabled'].index(node))
            elif drain_node['state'] == "active":
                self.properties['basic']['nodes'].pop(self.properties['basic']['nodes'].index(node))

        self._update()

        return self.nodes_status()

    def disable_node(self, node):
        """
        Disable a node in the pool

        Arguments:
            node (str): The node to disable

        Returns:
            (dict): Pool nodes status
        """
        # Make sure the node is in the pool
        disable_node = self.nodes.get(node, None)
        if disable_node is None:
            self._bad_node(node)

        disable_node['state'] = 'disabled'

        # Deal with the properties differences for versions 1.0 and 2.0
        if self.api_version in ['1.0', '2.0']:
            self.properties['basic']['disabled'].append(node)
            if disable_node['state'] == "draining":
                self.properties['basic']['draining'].pop(self.properties['basic']['draining'].index(node))
            elif disable_node['state'] == "active":
                self.properties['basic']['nodes'].pop(self.properties['basic']['nodes'].index(node))

        self._update()

        return self.nodes_status()

    def enable_node(self, node):
        """
        Reenable a node in the pool

        Arguments:
            node (str): The node to enable

        Returns:
            (dict): Pool nodes status
        """
        # Make sure the node is in the pool
        enable_node = self.nodes.get(node, None)
        if enable_node is None:
            self._bad_node(node)

        enable_node['state'] = 'active'

        # Deal with the properties differences for versions 1.0 and 2.0
        if self.api_version in ['1.0', '2.0']:
            self.properties['basic']['nodes'].append(node)
            if enable_node['state'] == "draining":
                self.properties['basic']['draining'].pop(self.properties['basic']['draining'].index(node))
            elif enable_node['state'] == "disabled":
                self.properties['basic']['disabled'].pop(self.properties['basic']['disabled'].index(node))

        self._update()

        return self.nodes_status()

    def delete_node(self, node):
        """
        Delete a node from the pool

        Arguments:
            node (str): The node to delete

        Returns:
            (dict): Pool nodes status
        """
        # Make sure the node is in the pool
        delete_node = self.nodes.get(node, None)
        if delete_node is None:
            self._bad_node(node)

        self.nodes.pop(node)

        # Deal with the properties differences for versions 1.0 and 2.0
        if self.api_version in ['1.0', '2.0']:
            if delete_node['state'] == "disabled":
                self.properties['basic']['disabled'].pop(self.properties['basic']['disabled'].index(node))
            elif delete_node['state'] == "draining":
                self.properties['basic']['draining'].pop(self.properties['basic']['draining'].index(node))
            else:
                self.properties['basic']['nodes'].pop(self.properties['basic']['nodes'].index(node))
        else:
            for i in range(len(self.properties['basic']['nodes_table'])):
                if self.properties['basic']['nodes_table'][i]['node'] == node:
                    self.properties['basic']['nodes_table'].pop(i)
                    break

        self._update()

        return self.nodes_status()

    def statistics(self):
        """
        Get statistics for the pool

        Returns:
            (dict): Pool statistics
        """
        return self.status_api.statistic('pools', self.name)

