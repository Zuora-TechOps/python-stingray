import apiclient_responses as ar
import pytest
from requests.exceptions import ConnectionError
import stingray.apiclient as sapi
from stingray.apiclient import StingrayAPIClientError, StingrayAPIClientAuthenticationError

stingray_args = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
)

api_json = {
    'children': [
        {
            'name': '4.0',
            'href': '/api/tm/4.0/'
        },
        {
            'name': '5.0',
            'href': '/api/tm/5.0/'
        },
        {
            'name': '5.1',
            'href': '/api/tm/5.1/'
        },
        {
            'name': '5.2',
            'href': '/api/tm/5.2/'
        }
    ]
}

client_base = 'https://stingray:9070/api/tm/'
status_base = client_base + '5.2/status/local_tm'

pytest_plugins = "pytest-responses"


def base_response(responses):
    responses.add(
        responses.GET,
        client_base,
        json=api_json,
    )


class TestStingrayClient(object):

    def test_client_init(self, responses):
        base_response(responses)

        sc = sapi.Client(**stingray_args)
        assert isinstance(sc, sapi.Client)
        assert sc.api_host == "stingray"
        assert sc.api_port == "9070"
        assert sc.api_user == "admin"
        assert sc.api_password == "admin"
        assert sc.api_version == "5.2"
        assert sc.ssl_verify

    def test_client_init_with_api_version(self):
        sc = sapi.Client(api_version='1.0', **stingray_args)
        assert sc.api_version == "1.0"

    def test_client_init_no_user(self):
        with pytest.raises(StingrayAPIClientAuthenticationError):
            sapi.Client(host='stingray', port='9070', password='admin')

    def test_client_init_no_connection(self, responses):
        responses.add(
            responses.GET,
            client_base,
            body=ConnectionError('Failed to establish a new connection: [Errno 110] Connection timed out',)
        )
        with pytest.raises(StingrayAPIClientError):
            sapi.Client(**stingray_args)

    def test_client_init_bad_auth_params(self, responses):
        responses.add(
            responses.GET,
            client_base,
            status=401,
            json=ar.auth_error,
        )
        with pytest.raises(StingrayAPIClientAuthenticationError):
            sapi.Client(**stingray_args)

    def test_client_api_path(self):
        sc = sapi.Client(api_version='5.2', **stingray_args)
        assert sc._api_path('/status/local_tm') == "5.2/status/local_tm"

    def test_client_get_supported_versions(self, responses):
        base_response(responses)

        sc = sapi.Client(api_version='5.2', **stingray_args)
        versions = sc.get_supported_versions()
        assert len(versions) == 4
        assert versions == ['4.0', '5.0', '5.1', '5.2']

    def test_client_get_config_endpoints(self, responses):
        responses.add(
            responses.GET,
            '{0}5.2/config/active/'.format(client_base),
            json=ar.config_endpoints
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        endpoints = sc.get_config_endpoints()
        assert len(endpoints) == 36
        assert endpoints['actions'] == "/api/tm/5.2/config/active/actions/"
        assert endpoints['pools'] == "/api/tm/5.2/config/active/pools/"

    def test_client_get_config_endpoints_old(self, responses):
        responses.add(
            responses.GET,
            '{0}1.0/config/active/'.format(client_base),
            json=ar.config_endpoints_v1
        )
        sc = sapi.Client(api_version='1.0', **stingray_args)
        endpoints = sc.get_config_endpoints()
        assert len(endpoints) == 27
        assert 'zxtms' in endpoints
        assert 'vservers' in endpoints
        assert endpoints['pools'] == "/api/tm/1.0/config/active/pools/"

    def test_client_get_status(self):
        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        assert isinstance(status, sapi.StatusAPI)

    def test_client_get_status_v1(self):
        sc = sapi.Client(api_version='1.0', **stingray_args)
        with pytest.raises(
                StingrayAPIClientError,
                match="API version 1.0 does not support the status endpoint"):
            sc.get_status()


class TestStingrayStatusAPI(object):

    def test_status_api_backups(self, responses):
        responses.add(
            responses.GET,
            '{0}/backups/full/'.format(status_base),
            json=ar.full_backups
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        backups = status.backups()
        assert backups[0]['name'] == "Backup1"

    def test_status_api_backup(self, responses):
        responses.add(
            responses.GET,
            '{0}/backups/full/Backup1'.format(status_base),
            json=ar.get_backup
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        backup_properties = status.backup('Backup1')
        assert backup_properties['description'] == "Test Backup"
        assert backup_properties['time_stamp'] == 1530257980
        assert backup_properties['version'] == "18.1"

    def test_status_api_information(self, responses):
        responses.add(
            responses.GET,
            '{0}/information'.format(status_base),
            json=ar.status_info
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        information = status.information()
        assert information['tm_version'] == "18.1"
        assert information['uuid'] == "c8cd17b3-f23e-3601-84e9-0a71387cf724"

    def test_status_api_statistics(self, responses):
        responses.add(
            responses.GET,
            '{0}/statistics/'.format(status_base),
            json=ar.statistics
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        stats_list = status.statistics()
        assert len(stats_list) == 23
        assert stats_list['nodes'] == "/api/tm/5.2/status/local_tm/statistics/nodes/"

    def test_status_api_statistics_globals(self, responses):
        responses.add(
            responses.GET,
            '{0}/statistics/globals'.format(status_base),
            json=ar.statistics_globals
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        global_stats = status.statistic('globals')
        assert len(global_stats) == 78
        assert global_stats['events_seen'] == 184658

    def test_status_api_statistics_type_list(self, responses):
        responses.add(
            responses.GET,
            '{0}/statistics/cache/'.format(status_base),
            json=ar.cache_stats
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        stats_list = status.statistic('cache')
        assert len(stats_list) == 7
        assert stats_list['web_cache'] == "/api/tm/5.2/status/local_tm/statistics/cache/web_cache"

    def test_status_api_statistics_type_stat(self, responses):
        responses.add(
            responses.GET,
            '{0}/statistics/cache/web_cache'.format(status_base),
            json=ar.web_cache
        )

        sc = sapi.Client(api_version='5.2', **stingray_args)
        status = sc.get_status()
        stats = status.statistic('cache', 'web_cache')
        assert len(stats) == 15
        assert stats['max_entries'] == 10000

