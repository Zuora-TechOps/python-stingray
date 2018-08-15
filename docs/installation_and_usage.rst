Installing and Using the ``stingray`` Module
============================================

Installation
------------

``pip install stingray``

Usage Examples
--------------

Connecting to a Stingray device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating a ``Client()`` object: ::

    In [1]: import stingray.apiclient as sapi

    In [2]: client = sapi.Client(host=stingray.example.com, port=9070, user=admin, password=admin.password, api_version=5.2, ssl_verify=False)

    In [3]: client.get_supported_versions()

    Out[3]: [u'4.0', u'5.0', u'5.1', u'5.2']

All of the arguments for creating a client object can be set as environment
variables so they don't have to be passed on a command line or included in
code. Environment variables are:

* STINGRAY_HOST
* STINGRAY_PORT
* STINGRAY_USER
* STINGRAY_PASSWORD
* STINGRAY_API_VERSION
* STINGRAY_SSL_VERIFY

If not given, ``port`` defaults to ``9070``, and ``ssl_verify`` defaults to
``True``. If no ``api_version`` is given the client will query the device for
supported versions and will choose the latest version available.

Device Statistics
^^^^^^^^^^^^^^^^^

*Note*: Status is not supported in API version 1.0

Get a ``StatusAPI()`` object from the client: ::

    In [1]: status = client.get_status()

Statistics for a load balancer pool: ::

    In [2]: status.statistic('pools', 'my_pool')

    Out [2]:
    {u'algorithm': u'roundrobin',
     u'bw_limit_bytes_drop': 0,
     u'bw_limit_pkts_drop': 0,
     u'bytes_in': 0,
     u'bytes_out': 0,
     u'conns_queued': 0,
     u'disabled': 0,
     u'draining': 0,
     u'max_queue_time': 0,
     u'mean_queue_time': 0,
     u'min_queue_time': 0,
     u'nodes': 1,
     u'persistence': u'none',
     u'queue_timeouts': 0,
     u'session_migrated': 0,
     u'state': u'active',
     u'total_conn': 0}

Pool Configurations
^^^^^^^^^^^^^^^^^^^

Get a ``Pools`` object: ::

    In [1]: from stingray.config.pools import Pools

    In [2]: pools = Pools.from_client(client)

List current pools: ::

    In [3]: pools.pools

    Out[3]:
    {u'Pool1': u'/api/tm/5.2/config/active/pools/Pool1',
     u'Pool2': u'/api/tm/5.2/config/active/pools/Pool2',
     u'Pool3': u'/api/tm/5.2/config/active/pools/Pool3'}

Add a new pool: ::

    In [4]: new_pool = pools.add('new_pool', nodes=['node1', 'node2'])

Configure a pool: ::

    In [5]: pool = pools.get('Pool1')

    In [6]: pool.nodes()

    Out [6]:
    {u'Node1': {u'node': u'Node1', u'state': u'active'},
     u'Node2': {u'node': u'Node2', u'state': u'active'}}

    In [7]: pool.drain_node('Node2')

    Out [7]:
    {u'Node1': {
       u'state': u'active',
       u'health': u'alive',
       u'connections': 9,
       u'requests': 0},
     u'Node2': {
       u'state': u'draining',
       u'health': u'alive',
       u'connections': 0,
       u'requests': 0}}

Update arbitrary pool properties: ::

    In [8]: pool.properties['connection']

    Out [9]:
    {u'max_connect_time': 4,
     u'max_connections_per_node': 0,
     u'max_queue_size': 0,
     u'max_reply_time': 30,
     u'queue_timeout': 10
    }

    In [10]: pool.properties['connection']['queue_timeout'] = 30

    In [11]: pool.update()

    In [12]: pool.properties['connection']

    Out [12]:
    {u'max_connect_time': 4,
     u'max_connections_per_node': 0,
     u'max_queue_size': 0,
     u'max_reply_time': 30,
     u'queue_timeout': 30
    }

