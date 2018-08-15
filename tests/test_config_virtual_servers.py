import copy
import json
import pytest
from stingray.apiclient import Client, StatusAPI, StingrayAPIClientError
from stingray.config.virtual_servers import VirtualServers, VirtualServer
import config_virtual_servers_responses as cvsr

stingray_args = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
    api_version='5.2',
)

stingray_args_v1 = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
    api_version='1.0',
)

base = 'https://stingray:9070/api/tm/5.2/config/active/'
stats_base = 'https://stingray:9070/api/tm/5.2/status/local_tm/statistics/'
base_v1 = 'https://stingray:9070/api/tm/1.0/config/active/'

pytest_plugins = "pytest-responses"


def base_response(responses):
    responses.add(
        responses.GET,
        '{0}virtual_servers/'.format(base),
        json=cvsr.virtual_servers,
    )


def base_response_v1(responses):
    responses.add(
        responses.GET,
        '{0}vservers/'.format(base_v1),
        json=cvsr.virtual_servers_v1,
    )


def responses_callback(responses, endpoint):
    responses.add_callback(
        responses.PUT,
        '{0}virtual_servers/{1}'.format(base, endpoint),
        callback=put_callback,
        content_type='application/json'
    )


def responses_callback_v1(responses, endpoint):
    responses.add_callback(
        responses.PUT,
        '{0}vservers/{1}'.format(base_v1, endpoint),
        callback=put_callback,
        content_type='application/json'
    )


def put_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')
    new_vs = copy.deepcopy(cvsr.get_vs)

    for section in rdata:
        for key, value in rdata[section].iteritems():
            new_vs[section][key] = value

    return (200, resp_headers, json.dumps(new_vs))


class TestStingrayVirtualServers(object):
    def test_config_virtual_servers_init(self, responses):
        base_response(responses)

        vss = VirtualServers(**stingray_args)
        assert isinstance(vss, VirtualServers)
        assert vss.config_path == "5.2/config/active/virtual_servers/"
        assert len(vss.virtual_servers) == 4
        assert vss.virtual_servers['Virtual Server 1'] == "/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%201"

    def test_config_virtual_servers_init_v1(self, responses):
        base_response_v1(responses)

        vss = VirtualServers(**stingray_args_v1)
        assert isinstance(vss, VirtualServers)
        assert vss.config_path == "1.0/config/active/vservers/"
        assert len(vss.virtual_servers) == 4
        assert vss.virtual_servers['Virtual Server 4'] == "/api/tm/1.0/config/active/vservers/Virtual%20Server%204"

    def test_config_virtual_servers_from_client(self, responses):
        base_response(responses)

        sc = Client(**stingray_args)
        vss = VirtualServers.from_client(sc)
        assert isinstance(vss, VirtualServers)
        assert vss.config_path == "5.2/config/active/virtual_servers/"
        assert len(vss.virtual_servers) == 4
        assert vss.virtual_servers['Virtual Server 2'] == "/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%202"

    def test_config_virtual_servers_get(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}virtual_servers/Virtual%20Server%201'.format(base),
            json=cvsr.get_vs
        )

        vss = VirtualServers(**stingray_args)
        vs = vss.get('Virtual Server 1')
        assert isinstance(vs, VirtualServer)

    def test_config_virtual_servers_get_bad(self, responses):
        base_response(responses)

        vss = VirtualServers(**stingray_args)
        with pytest.raises(
                StingrayAPIClientError,
                match="Virtual Server BadServer not found"):
            vss.get('BadServer')

    def test_config_virtual_servers_add(self, responses):
        base_response(responses)

        responses_callback(responses, 'Virtual%20Server%201')

        vss = VirtualServers(**stingray_args)
        vs = vss.add('Virtual Server 1', 'Pool1', 8000)
        assert isinstance(vs, VirtualServer)
        assert vs.properties['basic']['pool'] == "Pool1"
        assert vs.properties['basic']['port'] == 8000
        assert 'Virtual Server 1' in vss.virtual_servers

    def test_config_virtual_servers_add_v1(self, responses):
        base_response_v1(responses)

        responses_callback_v1(responses, 'Virtual%20Server%201')

        vss = VirtualServers(**stingray_args_v1)
        vs = vss.add('Virtual Server 1', 'Pool1', 8000)
        assert isinstance(vs, VirtualServer)
        assert vs.properties['basic']['pool'] == "Pool1"
        assert vs.properties['basic']['port'] == 8000
        assert 'Virtual Server 1' in vss.virtual_servers

    def test_config_virtual_servers_add_with_props(self, responses):
        base_response(responses)

        responses_callback(responses, 'Virtual%20Server%202')

        vss = VirtualServers(**stingray_args)
        vs = vss.add('Virtual Server 2', 'Pool2', 8000,
                     basic=dict(connect_timeout=30),
                     connection=dict(keepalive_timeout=30, timeoute=120))
        assert isinstance(vs, VirtualServer)
        assert vs.properties['basic']['pool'] == "Pool2"
        assert vs.properties['basic']['connect_timeout'] == 30
        assert vs.properties['connection']['keepalive_timeout'] == 30
        assert vs.properties['connection']['timeoute'] == 120

    def test_config_virtual_servers_delete(self, responses):
        base_response(responses)

        responses.add(
            responses.DELETE,
            '{0}virtual_servers/Virtual%20Server%203'.format(base),
            status=204
        )

        vss = VirtualServers(**stingray_args)
        del_response = vss.delete('Virtual Server 3')
        assert del_response['success'] == "Resource has been removed"


class TestStingrayVirtualServer(object):
    def test_config_virtual_server_init(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}virtual_servers/Virtual%20Server%201'.format(base),
            json=cvsr.get_vs
        )

        vss = VirtualServers(**stingray_args)
        vs = vss.get('Virtual Server 1')
        assert isinstance(vs, VirtualServer)
        assert vs.properties['basic']['pool'] == "Pool1"
        assert isinstance(vs.status_api, StatusAPI)

    def test_config_virtual_server_init_v1(self, responses):
        base_response_v1(responses)

        responses.add(
            responses.GET,
            '{0}vservers/Virtual%20Server%201'.format(base_v1),
            json=cvsr.get_vs
        )

        vss = VirtualServers(**stingray_args_v1)
        vs = vss.get('Virtual Server 1')
        assert isinstance(vs, VirtualServer)
        assert vs.properties['basic']['pool'] == "Pool1"
        assert vs.status_api is None

    def test_config_virtual_server_update(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}virtual_servers/Virtual%20Server%201'.format(base),
            json=cvsr.get_vs
        )

        responses_callback(responses, 'Virtual%20Server%201')

        vss = VirtualServers(**stingray_args)
        vs = vss.get('Virtual Server 1')
        vs.properties['basic']['connect_timeout'] = 120
        vs.update()
        assert vs.properties['basic']['connect_timeout'] == 120

    def test_config_virtual_server_statistics(self, responses):
        responses.add(
            responses.GET,
            '{0}virtual_servers/Virtual%20Server%201'.format(base),
            json=cvsr.get_vs
        )

        responses.add(
            responses.GET,
            '{0}virtual_servers/Virtual%20Server%201'.format(stats_base),
            json=cvsr.vs_stats
        )

        vs = VirtualServer('Virtual Server 1', **stingray_args)
        vs_stats = vs.statistics()
        assert vs_stats['port'] == 8000
        assert vs_stats['total_requests'] == 0
