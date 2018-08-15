from stingray.apiclient import Client, StingrayAPIClientError


class VirtualServers(Client):
    """
    Class for interacting with Virtual Servers via the REST API
    """
    def __init__(self, host=None, port=None, user=None, password=None,
                 api_version=None, ssl_verify=None):
        super(VirtualServers, self).__init__(host, port, user, password,
                                    api_version, ssl_verify)
        if self.api_version == "1.0":
            endpoint = 'vservers'
        else:
            endpoint = 'virtual_servers'
        self.config_path = '{0}/config/active/{1}/'.format(
            self.api_version,
            endpoint
        )
        self.virtual_servers = {}
        servers_list = self._api_get(self.config_path)
        for vs in servers_list['children']:
            self.virtual_servers[vs['name']] = vs['href']

    def __repr__(self):
        return '<Stingray Virtual Servers: {0}>'.format(self.api_host)

    @classmethod
    def from_client(cls, client):
        virtual_servers = cls(host=client.api_host, port=client.api_port,
                              user=client.api_user,
                              password=client.api_password,
                              api_version=client.api_version,
                              ssl_verify=client.ssl_verify)
        return virtual_servers

    def get(self, server):
        """
        Get a VirtualServer object for the requested virtual server

        Arguments:
            server (str): The name of the virtual server to get

        Returns:
            (VirtualServer): The requested virtual server
        """
        try:
            return VirtualServer.from_client(self, server,
                                             self.virtual_servers[server])
        except KeyError:
            raise StingrayAPIClientError(
                "Virtual Server {0} not found".format(server)
            )

    def add(self, server, pool, port, **server_props):
        """
        Add a new virtual server.

        Arguments:
            server (str): The virtual server name
            pool (str): The default pool to use for traffic
            port (int): The port to listen on
            server_props (dict): Additional arguments to set the properties
                of the virtual server at time of creation. Must be a dict
                in the form of: ::

                {'section': {'key': 'value'}}

        Returns:
            (VirtualServer): The new virtual server
        """
        virtual_server_data = dict(
            properties=dict(
                basic=dict(
                    pool=pool,
                    port=port,
                )
            )
        )

        for prop in server_props:
            virtual_server_data['properties'].setdefault(prop, dict())
            for key, value in server_props[prop].iteritems():
                virtual_server_data['properties'][prop][key] = value

        add_virtual_server_response = self._api_put(
            '{0}{1}'.format(self.config_path, server),
            virtual_server_data
        )

        vs = VirtualServer.from_client(
            self,
            server,
            server_path='{0}{1}'.format(self.config_path, server),
            server_properties=add_virtual_server_response['properties']
        )
        self.virtual_servers[server] = vs.config_path

        return vs

    def delete(self, server):
        """
        Delete a virtual server

        Arguments:
            server (str): The name of the virtual server to delete

        Returns:
            (dict): Response from the _api_delete method
        """
        delete_response = self._api_delete('{0}{1}'.format(
            self.config_path, server))

        if 'success' in delete_response:
            self.virtual_servers.pop(server)

        return delete_response


class VirtualServer(Client):
    """
    Class for interacting with individual virtual servers via the REST API
    """
    def __init__(self, server_name, server_path=None, server_properties=None,
                 host=None, port=None, user=None, password=None,
                 api_version=None, ssl_verify=None):
        super(VirtualServer, self).__init__(host, port, user, password,
                                            api_version, ssl_verify)
        self.name = server_name

        if server_path:
            self.config_path = server_path
        else:
            if self.api_version == "1.0":
                endpoint = 'vservers'
            else:
                endpoint = 'virtual_servers'

            self.config_path = '{0}/config/active/{1}/{2}'.format(
                self.api_version,
                endpoint,
                self.name
            )

        if server_properties:
            self.properties = server_properties
        else:
            server_properties = self._api_get(self.config_path)
            self.properties = server_properties['properties']

        try:
            self.status_api = self.get_status()
        except StingrayAPIClientError:
            self.status_api = None

    def __repr__(self):
        return '<Stingray Virtual Server {0}: {1}>'.format(
            self.name,
            self.api_host
        )

    @classmethod
    def from_client(cls, client, server_name, server_path=None,
                    server_properties=None):
        virtual_server = VirtualServer(server_name, server_path,
                                       server_properties, client.api_host,
                                       client.api_port, client.api_user,
                                       client.api_password, client.api_version,
                                       client.ssl_verify)
        return virtual_server

    def statistics(self):
        """
        Get statistics for the virtual server

        Returns:
            (dict): Virtual server statistics
        """
        if self.status_api is None:
            return []

        return self.status_api.statistic('virtual_servers', self.name)

