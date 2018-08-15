# -*- coding: utf-8 -*-

"""
Stingray/Zeus/Pulse Secure Load Balancer REST API Client Class
"""

import os
import requests
from requests.exceptions import ConnectionError
import urllib3


class StingrayAPIClientError(Exception):
    pass


class StingrayAPIClientAuthenticationError(Exception):
    pass


class Client(object):
    """Client class to access the Stingray REST API."""

    def __init__(self, host=None, port=None, user=None,
                 password=None, api_version=None, ssl_verify=None):
        """
        Create the client object to communicate with the REST API. The
        authentication, port, and ssl parameters can be pulled from the
        environment so that they don't have to be passed in from code
        or command line args.

        Arguments:
            host (str): Stingray host to connect to
            port (str): Port for the REST API, defaults to 9070
            user (str): Stingray admin user
            password (str): Admin user password
            api_version (str): Version of the API to use. Optional, will be
                derived from the API itself if not given.
            ssl_verify (bool): Whether to verify the SSL certificate or not.
                Set to false when using servers with self-signed certs.
        """

        self.api_host = host if host is not None else os.environ.get('STINGRAY_HOST', None)
        self.api_user = user if user is not None else os.environ.get('STINGRAY_USER', None)
        self.api_port = port if port is not None else os.environ.get('STINGRAY_PORT', '9070')
        self.api_password = password if password is not None else os.environ.get('STINGRAY_PASSWORD', None)
        self.ssl_verify = ssl_verify if ssl_verify is not None else os.environ.get('STINGRAY_SSL_VERIFY', True)
        self.api_version = api_version if api_version is not None else os.environ.get('STINGRAY_API_VERSION', None)
        self.api_headers = {"Content-Type": "application/json"}

        if self.api_user and self.api_password:
            self.api_headers.update(urllib3.make_headers(
                basic_auth="{0}:{1}".format(self.api_user, self.api_password)
            ))
        else:
            raise StingrayAPIClientAuthenticationError(
                "No username and/or password provided, cannot connect to the device"
            )

        if self.api_version is None:
            supported_versions = self.get_supported_versions()
            self.api_version = sorted(supported_versions)[-1]

        self.config_path = '{0}/config/active/'.format(self.api_version)

    def __repr__(self):
        return '<Stingray API Client: {0}>'.format(self.api_host)

    def _connection_error(self, error):
        raise StingrayAPIClientError(
            "Unable to connect to Stingray device {0}: {1}".format(
                self.api_host,
                str(error)
            )
        )

    def _handle_response(self, response):
        """
        Parse the response from the API and either return the data or raise
        an appropriate exception.
        """
        if response.status_code == 401:
            response_data = response.json()
            raise StingrayAPIClientAuthenticationError(
                "Authentication failed: {0}".format(
                    response_data.get('error_text', "Unknown")
                )
            )

        if not response.ok:
            try:
                response_data = response.json()
            except ValueError:
                raise StingrayAPIClientError(
                    "Connection to Stingray failed: {0} {1}".format(
                        response.status_code,
                        response.reason,
                    )
                )
            if response_data['error_id'] == "resource.not_found":
                raise StingrayAPIClientError(
                    "{0}, check supported API versions and endpoings".format(
                        response_data['error_text']
                    )
                )
            else:
                raise StingrayAPIClientError(
                    "Stingray API error {0}: {1}".format(
                        response_data['error_id'],
                        response_data['error_text']
                    )
                )

        return response.json()

    def _api_path(self, endpoint=None):
        """
        Prepare the API path as appropriate to pass to the REST endpoint.
        """
        path = ''
        if endpoint is not None:
            path += '{0}'.format(endpoint.lstrip('/'))
            path = path.replace('api/tm/', '')
            if not path.startswith(self.api_version):
                path = '/'.join([self.api_version, path])

        return path

    def _api_get(self, endpoint=None):
        """
        Send a GET request to the REST API.

        Arguments:
            endpoint (str): The endpoint to request, starting from the API
                            version.
        """
        path = self._api_path(endpoint)

        try:
            print "Fetching path {0}".format(path)
            response = requests.get(
                'https://{0}:{1}/api/tm/{2}'.format(
                    self.api_host,
                    self.api_port,
                    requests.utils.requote_uri(path)
                ),
                headers=self.api_headers,
                verify=self.ssl_verify,
            )
        except ConnectionError as e:
            self._connection_error(e)
        else:
            return self._handle_response(response)

    def _api_put(self, endpoint=None, data=None):
        """
        Send a PUT request to the REST API.

        Arguments:
            endpoint (str): The endpoint to request, starting from the API
                            version.
            data (dict): Data for the request.
        """
        path = self._api_path(endpoint)

        try:
            response = requests.put(
                'https://{0}:{1}/api/tm/{2}'.format(
                    self.api_host,
                    self.api_port,
                    requests.utils.requote_uri(path)
                ),
                headers=self.api_headers,
                verify=self.ssl_verify,
                json=data,
            )
        except ConnectionError as e:
            self._connection_error(e)
        else:
            return self._handle_response(response)

    def _api_delete(self, endpoint=None):
        """
        Send a DELETE request to the REST API.

        Arguments:
            endpoint (str): The endpoint to request, starting from the API
                            version.
        """
        path = self._api_path(endpoint)

        try:
            response = requests.delete(
                'https://{0}:{1}/api/tm/{2}'.format(
                    self.api_host,
                    self.api_port,
                    requests.utils.requote_uri(path)
                ),
                headers=self.api_headers,
                verify=self.ssl_verify,
            )
        except ConnectionError as e:
            self._connection_error(e)
        else:
            if response.status_code == 204:
                return dict(success="Resource has been removed")

            return self._handle_response(response)

    def update(self):
        """
        Convenience method to update the properties for an
        endpoint on the load balancer
        """
        updated = self._api_put(
            self.config_path, dict(properties=self.properties)
        )
        self.properties = updated['properties']

    def get_supported_versions(self):
        """
        Query the REST API for the version(s) it supports.

        Returns:
            (list): Supported versions
        """
        versions = []
        response_data = self._api_get()
        children = response_data.get('children', [])
        for child in children:
            versions.append(child['name'])

        return versions

    def get_config_endpoints(self):
        """
        Get all configuration endpoints.

        Returns:
            (dict): Endpoint names and paths
        """
        endpoints_list = self._api_get('{0}/config/active/'.format(
            self.api_version))
        endpoints = dict()
        for ep in endpoints_list['children']:
            endpoints[ep['name']] = ep['href']

        return endpoints

    def get_status(self):
        """
        Get a status object for the REST API ``status/local_tm/`` endpoint.

        Returns:
            (StatusAPI)
        """
        return StatusAPI.from_client(self)


class StatusAPI(Client):
    """
    Class for interacting with the ``status/local_tm/`` endpoints. Not supported
    in version 1.0 of the REST API
    """
    def __init__(self, host=None, port=None, user=None,
                 password=None, api_version=None, ssl_verify=None):
        super(StatusAPI, self).__init__(host, port, user,password,
                                        api_version, ssl_verify)

        self.status_path = '{0}/status/local_tm'.format(self.api_version)
        # Version 1.0 of the API has no status endpoint
        if self.api_version == "1.0":
            raise StingrayAPIClientError(
                "API version 1.0 does not support the status endpoint"
            )

    def __repr__(self):
        return '<Stingray StatusAPI: {0}>'.format(self.api_host)

    @classmethod
    def from_client(cls, client):
        status = cls(host=client.api_host, port=client.api_port,
                     user=client.api_user, password=client.api_password,
                     api_version=client.api_version,
                     ssl_verify=client.ssl_verify)
        return status

    def backups(self):
        """
        List current backups

        Returns:
            (list): List of dicts with backup name and path
        """
        backups_list = self._api_get('{0}/backups/full/'.format(
            self.status_path
        ))
        return backups_list['children']

    def backup(self, backup_name):
        """
        Get the properties of an individual backup

        Arguments:
            backup_name (str): The name of the backup to get

        Returns:
            (dict): Parameters for the backup
        """
        backup_properties = self._api_get('{0}/backups/full/{1}'.format(
            self.status_path,
            backup_name
        ))
        return backup_properties['properties']['backup']

    def information(self):
        """
        Get version and uuid for the load balancer.

        Returns:
            (dict): tm_version and uuid
        """
        information = self._api_get('{0}/information'.format(
            self.status_path
        ))
        return information['information']

    def state(self):
        """
        Get state information for load balancer components.

        Returns:
            (list): List of dicts with state for error level, errors, failed
                    nodes, license, pools, tip errors, and virtual servers
        """
        state_data = self._api_get('{0}/state'.format(
            self.status_path
        ))
        return state_data['state']

    def statistics(self):
        """
        Get the list of statistics for load balancer components

        Returns:
            (dict): Statistic type and path
        """
        statistics_list = self._api_get('{0}/statistics/'.format(
            self.status_path
        ))
        stats = dict()
        for stat in statistics_list['children']:
            stats[stat['name']] = stat['href']
        return stats

    def statistic(self, type, stat=None, stat_target=None):
        """
        Get either the list of statistics for an endpoint, or the statistic
        data. Some endpoints have nested children, some have multiple nested
        children.

        Arguments:
            type (str): The statistic type, or name, from the list of
                        available statistics, e.g. cache, pools, etc.
            stat (str): For single level nested stats, this is the name of the
                        stat to get information on. For multiple levels of
                        nesting this is the next level in the path.
            stat_target (str): For multiple level nested stats this is the
                               name of the stat to get information for.

        Returns:
            (dict): Available statistics for the type and their paths
            (dict): Data for the requested statistic
        """
        # globals and ssl_ocsp_stapling have no child stats, so we return
        # their data
        if type in ['globals', 'ssl_ocsp_stapling']:
            stats = self._api_get('{0}/statistics/{1}'.format(
                self.status_path,
                type
            ))
            return stats['statistics']

        # If we have the type argument, but not the stat, return the list of
        # available child stats.
        if stat is None:
            stats_list = self._api_get('{0}/statistics/{1}/'.format(
                self.status_path,
                type
            ))
            stats = dict()
            for s in stats_list['children']:
                stats[s['name']] = s['href']
            return stats

        # nodes, per_node_slm, and traffic_ips have another level
        # of child stats.
        if type in ['nodes', 'per_node_slm', 'traffic_ips']:
            # type and stat provided, but not target, so return the list of
            # child stats at this level.
            if stat_target is None:
                stats_list = self._api_get('{0}/statistics/{1}/{2}'.format(
                    self.status_path,
                    type,
                    stat,
                ))
                stats = dict()
                for s in stats_list['children']:
                    stats[s['name']] = s['href']
                return stats
            # type, stat, and stat_target provided, return the information
            # for the stat.
            stats = self._api_get('{0}/statistics/{1}/{2}/{3}'.format(
                self.status_path,
                type,
                stat,
                stat_target,
            ))
            return stats['statistics']

        # Other stats have a single level of child stats, so return the
        # information for the requested child stat.
        stats = self._api_get('{0}/statistics/{1}/{2}'.format(
            self.status_path,
            type,
            stat,
        ))
        return stats['statistics']
