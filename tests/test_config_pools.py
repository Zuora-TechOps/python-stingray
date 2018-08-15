import pytest
from stingray.apiclient import StingrayAPIClientError
from stingray.config.pools import Pools, Pool
import config_pool_responses as cpr

stingray_args = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
    api_version='5.2',
)

stingray_args_old = dict(
    host='stingray',
    port='9070',
    user='admin',
    password='admin',
    api_version='2.0',
)

pools_base = 'https://stingray:9070/api/tm/5.2/config/active/pools/'
stats_base = 'https://stingray:9070/api/tm/5.2/status/local_tm/statistics/'
pools_base_old = 'https://stingray:9070/api/tm/2.0/config/active/pools/'
stats_base_old = 'https://stingray:9070/api/tm/2.0/status/local_tm/statistics/'

pytest_plugins = "pytest-responses"


def base_response(responses):
    responses.add(
        responses.GET,
        pools_base,
        json=cpr.list_pools,
    )


def base_response_old(responses):
    responses.add(
        responses.GET,
        pools_base_old,
        json=cpr.list_pools_old,
    )


class TestStingrayPools(object):
    def test_config_pools_init(self, responses):
        base_response(responses)

        pools = Pools(**stingray_args)
        assert isinstance(pools, Pools)
        assert len(pools.pools) == 3
        assert pools.pools['Pool1'] == "/api/tm/5.2/config/active/pools/Pool1"

    def test_config_pools_init_old(self, responses):
        base_response_old(responses)

        pools = Pools(**stingray_args_old)
        assert isinstance(pools, Pools)
        assert pools.api_version == "2.0"

    def test_config_pools_get(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        node1 = pool.properties['basic']['nodes_table'][0]
        assert isinstance(pool, Pool)
        assert node1['node'] == "10.0.0.1:8000"
        assert node1['state'] == "active"
        assert node1['state'] == pool.nodes['10.0.0.1:8000']['state']

    def test_config_pools_get_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_old
        )

        pools = Pools(**stingray_args_old)
        assert pools.api_version == "2.0"

        pool = pools.get('Pool1')
        assert isinstance(pool, Pool)
        assert pool.api_version == "2.0"
        node1 = pool.properties['basic']['nodes'][0]
        assert node1 == "10.0.0.1:8000"
        assert pool.nodes[node1]['state'] == "active"

    def test_config_pools_add(self, responses):
        base_response(responses)

        responses.add(
            responses.PUT,
            '{0}Pool4'.format(pools_base),
            json=cpr.get_pool
        )

        pools = Pools(**stingray_args)
        new_pool = pools.add('Pool4', nodes=['10.0.0.1:8000'])
        assert isinstance(new_pool, Pool)
        assert new_pool.nodes.get('10.0.0.1:8000', False)
        assert 'Pool4' in pools.pools

    def test_config_pools_add_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.PUT,
            '{0}Pool4'.format(pools_base_old),
            json=cpr.get_pool_old
        )

        pools = Pools(**stingray_args_old)
        new_pool = pools.add('Pool4', nodes=['10.0.0.1:8000', '10.0.0.2:8000'])
        assert isinstance(new_pool, Pool)
        assert new_pool.nodes.get('10.0.0.1:8000', False)
        assert new_pool.properties['basic']['nodes'] == ['10.0.0.1:8000', '10.0.0.2:8000']
        assert 'Pool4' in pools.pools

    def test_config_pools_add_no_nodes(self, responses):
        base_response(responses)

        with pytest.raises(
                StingrayAPIClientError,
                match="No nodes specified, cannot create pool"):
            pools = Pools(**stingray_args)
            pools.add('Pool5')

    def test_config_pools_add_bad_arg(self, responses):
        base_response(responses)

        with pytest.raises(
                StingrayAPIClientError,
                match="Nodes must be specified as a list"):
            pools = Pools(**stingray_args)
            pools.add('Pool5', '10.0.0.2:8000')

    def test_config_pools_delete(self, responses):
        base_response(responses)

        responses.add(
            responses.DELETE,
            '{0}Pool1'.format(pools_base),
            status=204
        )

        pools = Pools(**stingray_args)
        del_response = pools.delete('Pool1')
        assert del_response['success'] == "Resource has been removed"
        assert 'Pool1' not in pools.pools


class TestStingrayPool(object):
    def test_config_pool_nodes_status(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        nodes_status = pool.nodes_status()
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert nodes_status['10.0.0.1:8000']['health'] == "alive"

    def test_config_pool_nodes_status_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_old
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base_old),
            json=cpr.nodes_status
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.2:8000'.format(stats_base_old),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        nodes_status = pool.nodes_status()
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert nodes_status['10.0.0.2:8000']['health'] == "alive"

    def test_config_pool_add_node(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base),
            json=cpr.two_nodes
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.2:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        assert len(pool.nodes) == 1

        nodes_status = pool.add_node('10.0.0.2:8000')
        assert '10.0.0.2:8000' in nodes_status
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert nodes_status['10.0.0.2:8000']['state'] == "active"
        assert len(pool.nodes) == 2
        assert len(pool.properties['basic']['nodes_table']) == 2

    def test_config_pool_add_node_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_old
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_add_old
        )
        for i in range(1, 4):
            responses.add(
                responses.GET,
                '{0}nodes/node/10.0.0.{1}:8000'.format(stats_base_old, i),
                json=cpr.nodes_status
            )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        assert len(pool.nodes) == 2

        nodes_status = pool.add_node('10.0.0.3:8000')
        assert nodes_status['10.0.0.3:8000']['state'] == "active"
        assert '10.0.0.3:8000' in pool.properties['basic']['nodes']
        assert len(pool.nodes) == 3
        assert len(pool.properties['load_balancing']['node_weighting']) == 3

    def test_config_pool_drain_node(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base),
            json=cpr.drain_node
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "active"

        nodes_status = pool.drain_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "draining"

    def test_config_pool_drain_node_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_add_old
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.drain_node_old
        )

        for i in range(1, 4):
            responses.add(
                responses.GET,
                '{0}nodes/node/10.0.0.{1}:8000'.format(stats_base_old, i),
                json=cpr.nodes_status
            )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "active"

        nodes_status = pool.drain_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "draining"
        assert '10.0.0.1:8000' in pool.properties['basic']['draining']

    def test_config_pool_drain_node_bad(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')

        with pytest.raises(
                StingrayAPIClientError,
                match="Node bad_node is not a member of this pool"):
            pool.drain_node('bad_node')

    def test_config_pool_disable_node(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.drain_node
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base),
            json=cpr.disable_node
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "draining"

        nodes_status = pool.disable_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "disabled"

    def test_config_pool_disable_node_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.drain_node_old
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.disable_node_old
        )

        for i in range(2, 4):
            responses.add(
                responses.GET,
                '{0}nodes/node/10.0.0.{1}:8000'.format(stats_base_old, i),
                json=cpr.nodes_status
            )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "draining"

        nodes_status = pool.disable_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "disabled"
        assert '10.0.0.1:8000' in pool.properties['basic']['disabled']

    def test_config_pool_disable_node_bad(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.drain_node
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        with pytest.raises(
                StingrayAPIClientError,
                match="Node bad_node is not a member of this pool"):
            pool.disable_node('bad_node')

    def test_config_pool_enable_node(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.disable_node
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "disabled"

        nodes_status = pool.enable_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert nodes_status['10.0.0.1:8000']['health'] == "alive"

    def test_config_pool_enable_node_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.disable_node_old
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_add_old
        )

        for i in range(1, 4):
            responses.add(
                responses.GET,
                '{0}nodes/node/10.0.0.{1}:8000'.format(stats_base_old, i),
                json=cpr.nodes_status
            )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        assert pool.nodes['10.0.0.1:8000']['state'] == "disabled"
        assert '10.0.0.1:8000' in pool.properties['basic']['disabled']

        nodes_status = pool.enable_node('10.0.0.1:8000')
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert pool.nodes['10.0.0.1:8000']['state'] == "active"
        assert '10.0.0.1:8000' in pool.properties['basic']['nodes']

    def test_config_pool_enable_node_bad(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.disable_node
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        with pytest.raises(
                StingrayAPIClientError,
                match="Node bad_node is not a member of this pool"):
            pool.enable_node('bad_node')

    def test_config_pool_delete_node(self, responses):
        base_response(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base),
            json=cpr.two_nodes
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base),
            json=cpr.get_pool
        )

        responses.add(
            responses.GET,
            '{0}nodes/node/10.0.0.1:8000'.format(stats_base),
            json=cpr.nodes_status
        )

        pools = Pools(**stingray_args)
        pool = pools.get('Pool1')
        assert len(pool.nodes) == 2

        nodes_status = pool.delete_node('10.0.0.2:8000')
        assert '10.0.0.2:8000' not in nodes_status
        assert nodes_status['10.0.0.1:8000']['state'] == "active"
        assert len(pool.nodes) == 1
        assert len(pool.properties['basic']['nodes_table']) == 1

    def test_config_pool_delete_node_old(self, responses):
        base_response_old(responses)

        responses.add(
            responses.GET,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_add_old
        )

        responses.add(
            responses.PUT,
            '{0}Pool1'.format(pools_base_old),
            json=cpr.get_pool_old
        )

        for i in range(1, 3):
            responses.add(
                responses.GET,
                '{0}nodes/node/10.0.0.{1}:8000'.format(stats_base_old, i),
                json=cpr.nodes_status
            )

        pools = Pools(**stingray_args_old)
        pool = pools.get('Pool1')
        assert len(pool.nodes) == 3
        assert len(pool.properties['basic']['nodes']) == 3
        assert '10.0.0.3:8000' in pool.properties['basic']['nodes']

        nodes_status = pool.delete_node('10.0.0.3:8000')
        assert sorted(nodes_status.keys()) == ['10.0.0.1:8000', '10.0.0.2:8000']
        assert len(pool.nodes) == 2
        assert len(pool.properties['basic']['nodes']) == 2
        assert '10.0.0.3:8000' not in pool.nodes
        assert '10.0.0.3:8000' not in pool.properties['basic']['nodes']
