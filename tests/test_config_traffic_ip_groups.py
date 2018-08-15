import copy
import json
import pytest
from stingray.apiclient import Client, StatusAPI, StingrayAPIClientError
from stingray.config.traffic_ip_groups import TrafficIPGroups, TrafficIPGroup
import config_traffic_ip_groups_responses as ctigr

stingray_args = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
    api_version='5.2',
)

base = 'https://stingray:9070/api/tm/5.2/config/active/traffic_ip_groups/'
stats_base = 'https://stingray:9070/api/tm/5.2/status/local_tm/statistics/'

pytest_plugins = "pytest-responses"


def base_response(responses):
    responses.add(
        responses.GET,
        '{0}'.format(base),
        json=ctigr.traffic_ip_groups,
    )


def responses_callback(responses, endpoint):
    responses.add_callback(
        responses.PUT,
        '{0}{1}'.format(base, endpoint),
        callback=put_callback,
        content_type='application/json'
    )


def put_callback(request):
    rdata = json.loads(request.body)
    resp_headers = dict(ContentType='application/json')
    new_tig = copy.deepcopy(ctigr.traffic_ip_group)

    for section in rdata:
        for key, value in rdata[section].iteritems():
            new_tig[section][key] = value

    return (200, resp_headers, json.dumps(new_tig))


class TestTrafficIPGroups(object):
    def test_config_traffic_ip_groups_init(self, responses):
        base_response(responses)

        tigs = TrafficIPGroups(**stingray_args)
        assert isinstance(tigs, TrafficIPGroups)
        assert tigs.config_path == "5.2/config/active/traffic_ip_groups/"
        assert len(tigs.traffic_ip_groups) == 3
        assert tigs.traffic_ip_groups['www.example.com'] == "/api/tm/5.2/config/active/traffic_ip_groups/www.example.com"

    def test_config_traffic_ip_groups_init_from_client(self, responses):
        base_response(responses)

        sc = Client(**stingray_args)
        tigs = TrafficIPGroups.from_client(sc)
        assert isinstance(tigs, TrafficIPGroups)
        assert tigs.config_path == "5.2/config/active/traffic_ip_groups/"
        assert len(tigs.traffic_ip_groups) == 3
        assert tigs.traffic_ip_groups['www.example.com'] == "/api/tm/5.2/config/active/traffic_ip_groups/www.example.com"

    def test_config_traffic_ip_groups_get(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}www.example.com'.format(base),
            json=ctigr.traffic_ip_group
        )

        tigs = TrafficIPGroups(**stingray_args)
        tig = tigs.get('www.example.com')
        assert isinstance(tig, TrafficIPGroup)

    def test_config_traffic_ip_groups_get_bad(self, responses):
        base_response(responses)

        tigs = TrafficIPGroups(**stingray_args)
        with pytest.raises(
                StingrayAPIClientError,
                match="Traffic IP Group BadGroup not found"):
            tigs.get('BadGroup')

    def test_config_traffic_ip_groups_add(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            'https://stingray:9070/api/tm/5.2/config/active/traffic_managers',
            json=ctigr.traffic_managers
        )

        responses_callback(responses, 'TestGroup')

        tigs = TrafficIPGroups(**stingray_args)
        tig = tigs.add('TestGroup', ipaddresses=['192.168.100.2'])
        assert len(tigs.traffic_ip_groups) == 4
        assert tig.name in tigs.traffic_ip_groups
        assert isinstance(tig, TrafficIPGroup)

    def test_config_traffic_ip_groups_add_with_props(self, responses):
        base_response(responses)

        responses_callback(responses, 'TestGroup')

        tigs = TrafficIPGroups(**stingray_args)
        tig = tigs.add('TestGroup', ipaddresses=['192.168.100.2'],
                       machines=[tigs.api_host], mode='ec2vpcelastic',
                       basic=dict(ip_assignment_mode='alphabetic'))
        assert isinstance(tig, TrafficIPGroup)
        assert tig.properties['basic']['ip_assignment_mode'] == "alphabetic"
        assert tig.properties['basic']['mode'] == "ec2vpcelastic"

    def test_config_traffic_ip_groups_add_bad_args(self, responses):
        base_response(responses)

        tigs = TrafficIPGroups(**stingray_args)
        with pytest.raises(
                StingrayAPIClientError,
                match="No IP addresses specified, unable to create Traffic IP group"):
            tigs.add('TestGroup')

    def test_config_traffic_ip_groups_delete(self, responses):
        base_response(responses)

        responses.add(
            responses.DELETE,
            '{0}www.example.com'.format(base),
            status=204
        )

        tigs = TrafficIPGroups(**stingray_args)
        del_response = tigs.delete('www.example.com')
        assert del_response['success'] == "Resource has been removed"
        assert len(tigs.traffic_ip_groups) == 2
        assert 'www.example.com' not in tigs.traffic_ip_groups


class TestTrafficIPGroup(object):
    def test_config_traffic_ip_group_init(self, responses):
        responses.add(
            responses.GET,
            '{0}www.example.com'.format(base),
            json=ctigr.traffic_ip_group
        )

        tig = TrafficIPGroup('www.example.com', **stingray_args)
        assert isinstance(tig, TrafficIPGroup)
        assert tig.config_path == "5.2/config/active/traffic_ip_groups/www.example.com"
        assert tig.properties['basic']['ipaddresses'] == ['192.168.100.1']
        assert tig.properties['basic']['machines'] == ['10.0.0.1']

    def test_config_traffic_ip_group_update(self, responses):
        responses.add(
            responses.GET,
            '{0}www.example.com'.format(base),
            json=ctigr.traffic_ip_group
        )

        responses_callback(responses, 'www.example.com')

        tig = TrafficIPGroup('www.example.com', **stingray_args)
        tig.properties['basic']['ip_assignment_mode'] = "alphabetic"
        tig.update()
        assert tig.properties['basic']['ip_assignment_mode'] == "alphabetic"

    def test_config_traffic_ip_group_statistics(self, responses):
        responses.add(
            responses.GET,
            '{0}www.example.com'.format(base),
            json=ctigr.traffic_ip_group
        )

        responses.add(
            responses.GET,
            '{0}traffic_ips/traffic_ip/192.168.100.1'.format(stats_base),
            json=ctigr.traffic_ip_stats
        )

        tig = TrafficIPGroup('www.example.com', **stingray_args)
        tig_stats = tig.statistics()
        assert tig_stats['192.168.100.1']['state'] == "lowered"
        assert tig_stats['192.168.100.1']['time'] == 730457300
