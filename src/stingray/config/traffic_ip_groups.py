from stingray.apiclient import Client, StingrayAPIClientError


class TrafficIPGroups(Client):
    """
    Class for interacting with Traffic IP Groups via the REST API
    """
    def __init__(self, host=None, port=None, user=None, password=None,
                 api_version=None, ssl_verify=None):
        super(TrafficIPGroups, self).__init__(host, port, user, password,
                                              api_version, ssl_verify)

        if api_version == "1.0":
            raise StingrayAPIClientError(
                "API version 1.0 does not support Traffic IP Groups"
            )

        self.config_path = '{0}/config/active/traffic_ip_groups/'.format(
            self.api_version,
        )
        self.traffic_ip_groups = {}
        tigs_list = self._api_get(self.config_path)
        for tig in tigs_list['children']:
            self.traffic_ip_groups[tig['name']] = tig['href']

    def __repr__(self):
        return '<Stingray Traffic IP Groups: {0}>'.format(self.api_host)

    @classmethod
    def from_client(cls, client):
        traffic_ip_groups = cls(host=client.api_host, port=client.api_port,
                                user=client.api_user,
                                password=client.api_password,
                                api_version=client.api_version,
                                ssl_verify=client.ssl_verify)
        return traffic_ip_groups

    def get(self, group):
        """
        Get a TrafficIPGroup object for the requested traffic ip group

        Arguments:
            group (str): The name of the traffic ip group to get

        Returns:
            (TrafficIPGroup): The requested traffic ip group
        """
        try:
            return TrafficIPGroup.from_client(self, group,
                                              self.traffic_ip_groups[group])
        except KeyError:
            raise StingrayAPIClientError(
                "Traffic IP Group {0} not found".format(group)
            )

    def add(self, group, ipaddresses=None, machines=None,
            mode='singlehosted', **group_props):
        """
        Add a new traffic ip group.

        Arguments:
            group (str): The traffic ip group name
            ipaddresses (list): IP addresses to assign to the group
            machines (list): Load balancers that can host the group's
                IP addresses. Default is the current load balancer (or load
                balancers if clustered).
            mode (str): Method used to distribute traffic across the cluster.
                Default is ``singlehosted``
            group_props (dict): Additional arguments to set the properties
                of the traffic ip group at time of creation. Must be a
                dict in the form of: ::

                {'section': {'key': 'value'}}

        Returns:
            (TrafficIPGroup): The new traffic ip group
        """
        if ipaddresses is None:
            raise StingrayAPIClientError(
                "No IP addresses specified, unable to create Traffic IP group"
            )

        if machines is None:
            machines = []
            tm_list = self._api_get('config/active/traffic_managers')
            for tm in tm_list['children']:
                machines.append(tm['name'])

        traffic_ip_group_data = dict(
            properties=dict(
                basic=dict(
                    ipaddresses=ipaddresses,
                    machines=machines,
                    mode=mode
                )
            )
        )

        for prop in group_props:
            traffic_ip_group_data['properties'].setdefault(prop, dict())
            for key, value in group_props[prop].iteritems():
                traffic_ip_group_data['properties'][prop][key] = value

        add_traffic_ip_group_response = self._api_put(
            '{0}{1}'.format(self.config_path, group),
            traffic_ip_group_data
        )

        tig = TrafficIPGroup.from_client(
            self,
            group,
            group_path='{0}{1}'.format(self.config_path, group),
            group_properties=add_traffic_ip_group_response['properties']
        )
        self.traffic_ip_groups[group] = tig.config_path

        return tig

    def delete(self, group):
        """
        Delete a traffic ip group

        Arguments:
            group (str): The name of the traffic ip group to delete

        Returns:
            (dict): Response from the _api_delete method
        """
        delete_response = self._api_delete('{0}{1}'.format(self.config_path, group))
        if 'success' in delete_response:
            self.traffic_ip_groups.pop(group)

        return delete_response


class TrafficIPGroup(Client):
    """
    Class for interacting with individual traffic ip groups via the REST API
    """
    def __init__(self, group_name, group_path=None, group_properties=None,
                 host=None, port=None, user=None, password=None,
                 api_version=None, ssl_verify=None):
        super(TrafficIPGroup, self).__init__(host, port, user, password,
                                             api_version, ssl_verify)
        self.name = group_name

        if group_path:
            self.config_path = group_path
        else:
            self.config_path = '{0}/config/active/traffic_ip_groups/{1}'.format(
                self.api_version,
                self.name
            )

        if group_properties:
            self.properties = group_properties
        else:
            group_properties = self._api_get(self.config_path)
            self.properties = group_properties['properties']

        try:
            self.status_api = self.get_status()
        except StingrayAPIClientError:
            self.status_api = None

    def __repr__(self):
        return '<Stingray Traffic IP Group {0}: {1}>'.format(
            self.name,
            self.api_host
        )

    @classmethod
    def from_client(cls, client, group_name, group_path=None,
                    group_properties=None):
        traffic_ip_group = TrafficIPGroup(group_name, group_path,
                                          group_properties, client.api_host,
                                          client.api_port, client.api_user,
                                          client.api_password, client.api_version,
                                          client.ssl_verify)
        return traffic_ip_group

    def statistics(self):
        """
        Get statistics for the traffic ips in the group

        Returns:
            (dict): Traffic IP statistics
        """
        if self.status_api is None:
            return []

        ip_stats = dict()
        for ip in self.properties['basic']['ipaddresses']:
            try:
                ip_stats[ip] = self.status_api.statistic(
                    'traffic_ips',
                    'traffic_ip',
                    ip
                )
            except StingrayAPIClientError:
                ip_stats[ip] = None

        return ip_stats
