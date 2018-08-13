list_pools = {
    u'children': [
        {
            u'name': 'Pool1',
            u'href': '/api/tm/5.2/config/active/pools/Pool1'
        },
        {
            u'name': 'Pool2',
            u'href': '/api/tm/5.2/config/active/pools/Pool2'
        },
        {
            u'name': 'Pool3',
            u'href': '/api/tm/5.2/config/active/pools/Pool3'
        }
    ]
}

list_pools_old = {
    u'children': [
        {
            u'name': 'Pool1',
            u'href': '/api/tm/2.0/config/active/pools/Pool1'
        },
        {
            u'name': 'Pool2',
            u'href': '/api/tm/2.0/config/active/pools/Pool2'
        },
        {
            u'name': 'Pool3',
            u'href': '/api/tm/2.0/config/active/pools/Pool3'
        }
    ]
}

get_pool = {
    u'properties': {
        u'auto_scaling': {
            u'addnode_delaytime': 0,
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'securitygroupids': [],
            u'size_id': u'',
            u'subnetids': []
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [u'Ping'],
            u'node_close_with_rst': False,
            u'node_connection_attempts': 3,
            u'node_delete_behavior': u'immediate',
            u'node_drain_to_delete_timeout': 0,
            u'nodes_table': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'state': u'active',
                    u'priority': 1,
                    u'weight': 1
                }
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'dns_autoscale': {
            u'enabled': False,
            u'hostnames': [],
            u'port': 80
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'kerberos_protocol_transition': {
            u'principal': u'',
            u'target': u''
        },
        u'l4accel': {
            u'snat': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'priority_enabled': False,
            u'priority_nodes': 1
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'service_discovery': {
            u'enabled': False,
            u'interval': 10,
            u'plugin': u'',
            u'plugin_args': u'',
            u'timeout': 0
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'cipher_suites': u'',
            u'client_auth': False,
            u'common_name_match': [],
            u'elliptic_curves': [],
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': True,
            u'server_name': False,
            u'session_cache_enabled': u'use_default',
            u'session_tickets_enabled': u'use_default',
            u'signature_algorithms': u'',
            u'strict_verify': False,
            u'support_ssl3': u'use_default',
            u'support_tls1': u'use_default',
            u'support_tls1_1': u'use_default',
            u'support_tls1_2': u'use_default'
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u'',
            u'response_timeout': 0
        }
    }
}

two_nodes = {
    u'properties': {
        u'auto_scaling': {
            u'addnode_delaytime': 0,
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'securitygroupids': [],
            u'size_id': u'',
            u'subnetids': []
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [u'Ping'],
            u'node_close_with_rst': False,
            u'node_connection_attempts': 3,
            u'node_delete_behavior': u'immediate',
            u'node_drain_to_delete_timeout': 0,
            u'nodes_table': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'state': u'active',
                    u'priority': 1,
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.2:8000',
                    u'state': u'active',
                    u'priority': 1,
                    u'weight': 1
                }
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'dns_autoscale': {
            u'enabled': False,
            u'hostnames': [],
            u'port': 80
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'kerberos_protocol_transition': {
            u'principal': u'',
            u'target': u''
        },
        u'l4accel': {
            u'snat': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'priority_enabled': False,
            u'priority_nodes': 1
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'service_discovery': {
            u'enabled': False,
            u'interval': 10,
            u'plugin': u'',
            u'plugin_args': u'',
            u'timeout': 0
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'cipher_suites': u'',
            u'client_auth': False,
            u'common_name_match': [],
            u'elliptic_curves': [],
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': True,
            u'server_name': False,
            u'session_cache_enabled': u'use_default',
            u'session_tickets_enabled': u'use_default',
            u'signature_algorithms': u'',
            u'strict_verify': False,
            u'support_ssl3': u'use_default',
            u'support_tls1': u'use_default',
            u'support_tls1_1': u'use_default',
            u'support_tls1_2': u'use_default'
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u'',
            u'response_timeout': 0
        }
    }
}

drain_node = {
    u'properties': {
        u'auto_scaling': {
            u'addnode_delaytime': 0,
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'securitygroupids': [],
            u'size_id': u'',
            u'subnetids': []
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [u'Ping'],
            u'node_close_with_rst': False,
            u'node_connection_attempts': 3,
            u'node_delete_behavior': u'immediate',
            u'node_drain_to_delete_timeout': 0,
            u'nodes_table': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'state': u'draining',
                    u'priority': 1,
                    u'weight': 1
                }
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'dns_autoscale': {
            u'enabled': False,
            u'hostnames': [],
            u'port': 80
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'kerberos_protocol_transition': {
            u'principal': u'',
            u'target': u''
        },
        u'l4accel': {
            u'snat': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'priority_enabled': False,
            u'priority_nodes': 1
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'service_discovery': {
            u'enabled': False,
            u'interval': 10,
            u'plugin': u'',
            u'plugin_args': u'',
            u'timeout': 0
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'cipher_suites': u'',
            u'client_auth': False,
            u'common_name_match': [],
            u'elliptic_curves': [],
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': True,
            u'server_name': False,
            u'session_cache_enabled': u'use_default',
            u'session_tickets_enabled': u'use_default',
            u'signature_algorithms': u'',
            u'strict_verify': False,
            u'support_ssl3': u'use_default',
            u'support_tls1': u'use_default',
            u'support_tls1_1': u'use_default',
            u'support_tls1_2': u'use_default'
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u'',
            u'response_timeout': 0
        }
    }
}

disable_node = {
    u'properties': {
        u'auto_scaling': {
            u'addnode_delaytime': 0,
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'securitygroupids': [],
            u'size_id': u'',
            u'subnetids': []
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [u'Ping'],
            u'node_close_with_rst': False,
            u'node_connection_attempts': 3,
            u'node_delete_behavior': u'immediate',
            u'node_drain_to_delete_timeout': 0,
            u'nodes_table': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'state': u'disabled',
                    u'priority': 1,
                    u'weight': 1
                }
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'dns_autoscale': {
            u'enabled': False,
            u'hostnames': [],
            u'port': 80
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'kerberos_protocol_transition': {
            u'principal': u'',
            u'target': u''
        },
        u'l4accel': {
            u'snat': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'priority_enabled': False,
            u'priority_nodes': 1
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'service_discovery': {
            u'enabled': False,
            u'interval': 10,
            u'plugin': u'',
            u'plugin_args': u'',
            u'timeout': 0
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'cipher_suites': u'',
            u'client_auth': False,
            u'common_name_match': [],
            u'elliptic_curves': [],
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': True,
            u'server_name': False,
            u'session_cache_enabled': u'use_default',
            u'session_tickets_enabled': u'use_default',
            u'signature_algorithms': u'',
            u'strict_verify': False,
            u'support_ssl3': u'use_default',
            u'support_tls1': u'use_default',
            u'support_tls1_1': u'use_default',
            u'support_tls1_2': u'use_default'
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u'',
            u'response_timeout': 0
        }
    }
}

pool_status = {
    u'statistics': {
        u'algorithm': u'roundrobin',
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
        u'total_conn': 0
    }
}

nodes_status = {
    u'statistics': {
        u'current_conn': 0,
        u'current_requests': 0,
        u'errors': 0,
        u'failures': 0,
        u'new_conn': 0,
        u'pooled_conn': 0,
        u'port': 8000,
        u'response_max': 0,
        u'response_mean': 0,
        u'response_min': 0,
        u'state': u'alive',
        u'total_conn': 0
    }
}

get_pool_old = {
    u'properties': {
        u'auto_scaling': {
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'size_id': u''
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'disabled': [],
            u'draining': [],
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [
                u'Ping'
            ],
            u'node_connection_attempts': 3,
            u'nodes': [
                u'10.0.0.1:8000',
                u'10.0.0.2:8000'
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'node_weighting': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.2:8000',
                    u'weight': 1
                }
            ],
            u'priority_enabled': False,
            u'priority_nodes': 1,
            u'priority_values': []
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'client_auth': False,
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': False,
            u'server_name': False,
            u'strict_verify': False
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u''
        }
    }
}

get_pool_add_old = {
    u'properties': {
        u'auto_scaling': {
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'size_id': u''
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'disabled': [],
            u'draining': [],
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [
                u'Ping'
            ],
            u'node_connection_attempts': 3,
            u'nodes': [
                u'10.0.0.1:8000',
                u'10.0.0.2:8000',
                u'10.0.0.3:8000'
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'node_weighting': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.2:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.3:8000',
                    u'weight': 1
                }
            ],
            u'priority_enabled': False,
            u'priority_nodes': 1,
            u'priority_values': []
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'client_auth': False,
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': False,
            u'server_name': False,
            u'strict_verify': False
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u''
        }
    }
}

drain_node_old = {
    u'properties': {
        u'auto_scaling': {
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'size_id': u''
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'disabled': [],
            u'draining': [
                u'10.0.0.1:8000'
            ],
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [
                u'Ping'
            ],
            u'node_connection_attempts': 3,
            u'nodes': [
                u'10.0.0.2:8000',
                u'10.0.0.3:8000'
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'node_weighting': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.2:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.3:8000',
                    u'weight': 1
                }
            ],
            u'priority_enabled': False,
            u'priority_nodes': 1,
            u'priority_values': []
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'client_auth': False,
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': False,
            u'server_name': False,
            u'strict_verify': False
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u''
        }
    }
}

disable_node_old = {
    u'properties': {
        u'auto_scaling': {
            u'cloud_credentials': u'',
            u'cluster': u'',
            u'data_center': u'',
            u'data_store': u'',
            u'enabled': False,
            u'external': True,
            u'hysteresis': 20,
            u'imageid': u'',
            u'ips_to_use': u'publicips',
            u'last_node_idle_time': 3600,
            u'max_nodes': 4,
            u'min_nodes': 1,
            u'name': u'',
            u'port': 80,
            u'refractory': 180,
            u'response_time': 1000,
            u'scale_down_level': 95,
            u'scale_up_level': 40,
            u'size_id': u''
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'disabled': [
                u'10.0.0.1:8000'
            ],
            u'draining': [],
            u'failure_pool': u'',
            u'max_connection_attempts': 0,
            u'max_idle_connections_pernode': 50,
            u'max_timed_out_connection_attempts': 2,
            u'monitors': [
                u'Ping'
            ],
            u'node_connection_attempts': 3,
            u'nodes': [
                u'10.0.0.2:8000',
                u'10.0.0.3:8000'
            ],
            u'note': u'',
            u'passive_monitoring': True,
            u'persistence_class': u'',
            u'transparent': False
        },
        u'connection': {
            u'max_connect_time': 4,
            u'max_connections_per_node': 0,
            u'max_queue_size': 0,
            u'max_reply_time': 30,
            u'queue_timeout': 10
        },
        u'ftp': {
            u'support_rfc_2428': False
        },
        u'http': {
            u'keepalive': True,
            u'keepalive_non_idempotent': False
        },
        u'load_balancing': {
            u'algorithm': u'round_robin',
            u'node_weighting': [
                {
                    u'node': u'10.0.0.1:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.2:8000',
                    u'weight': 1
                },
                {
                    u'node': u'10.0.0.3:8000',
                    u'weight': 1
                }
            ],
            u'priority_enabled': False,
            u'priority_nodes': 1,
            u'priority_values': []
        },
        u'node': {
            u'close_on_death': False,
            u'retry_fail_time': 60
        },
        u'smtp': {
            u'send_starttls': True
        },
        u'ssl': {
            u'client_auth': False,
            u'enable': False,
            u'enhance': False,
            u'send_close_alerts': False,
            u'server_name': False,
            u'strict_verify': False
        },
        u'tcp': {
            u'nagle': True
        },
        u'udp': {
            u'accept_from': u'dest_only',
            u'accept_from_mask': u''
        }
    }
}
