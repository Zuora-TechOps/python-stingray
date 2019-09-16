list_pools = {
    'children': [
        {
            'name': 'Pool1',
            'href': '/api/tm/5.2/config/active/pools/Pool1'
        },
        {
            'name': 'Pool2',
            'href': '/api/tm/5.2/config/active/pools/Pool2'
        },
        {
            'name': 'Pool3',
            'href': '/api/tm/5.2/config/active/pools/Pool3'
        }
    ]
}

list_pools_old = {
    'children': [
        {
            'name': 'Pool1',
            'href': '/api/tm/2.0/config/active/pools/Pool1'
        },
        {
            'name': 'Pool2',
            'href': '/api/tm/2.0/config/active/pools/Pool2'
        },
        {
            'name': 'Pool3',
            'href': '/api/tm/2.0/config/active/pools/Pool3'
        }
    ]
}

get_pool = {
    'properties': {
        'auto_scaling': {
            'addnode_delaytime': 0,
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'securitygroupids': [],
            'size_id': '',
            'subnetids': []
        },
        'basic': {
            'bandwidth_class': '',
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': ['Ping'],
            'node_close_with_rst': False,
            'node_connection_attempts': 3,
            'node_delete_behavior': 'immediate',
            'node_drain_to_delete_timeout': 0,
            'nodes_table': [
                {
                    'node': '10.0.0.1:8000',
                    'state': 'active',
                    'priority': 1,
                    'weight': 1
                }
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'dns_autoscale': {
            'enabled': False,
            'hostnames': [],
            'port': 80
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'kerberos_protocol_transition': {
            'principal': '',
            'target': ''
        },
        'l4accel': {
            'snat': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'priority_enabled': False,
            'priority_nodes': 1
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'service_discovery': {
            'enabled': False,
            'interval': 10,
            'plugin': '',
            'plugin_args': '',
            'timeout': 0
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'cipher_suites': '',
            'client_auth': False,
            'common_name_match': [],
            'elliptic_curves': [],
            'enable': False,
            'enhance': False,
            'send_close_alerts': True,
            'server_name': False,
            'session_cache_enabled': 'use_default',
            'session_tickets_enabled': 'use_default',
            'signature_algorithms': '',
            'strict_verify': False,
            'support_ssl3': 'use_default',
            'support_tls1': 'use_default',
            'support_tls1_1': 'use_default',
            'support_tls1_2': 'use_default'
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': '',
            'response_timeout': 0
        }
    }
}

two_nodes = {
    'properties': {
        'auto_scaling': {
            'addnode_delaytime': 0,
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'securitygroupids': [],
            'size_id': '',
            'subnetids': []
        },
        'basic': {
            'bandwidth_class': '',
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': ['Ping'],
            'node_close_with_rst': False,
            'node_connection_attempts': 3,
            'node_delete_behavior': 'immediate',
            'node_drain_to_delete_timeout': 0,
            'nodes_table': [
                {
                    'node': '10.0.0.1:8000',
                    'state': 'active',
                    'priority': 1,
                    'weight': 1
                },
                {
                    'node': '10.0.0.2:8000',
                    'state': 'active',
                    'priority': 1,
                    'weight': 1
                }
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'dns_autoscale': {
            'enabled': False,
            'hostnames': [],
            'port': 80
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'kerberos_protocol_transition': {
            'principal': '',
            'target': ''
        },
        'l4accel': {
            'snat': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'priority_enabled': False,
            'priority_nodes': 1
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'service_discovery': {
            'enabled': False,
            'interval': 10,
            'plugin': '',
            'plugin_args': '',
            'timeout': 0
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'cipher_suites': '',
            'client_auth': False,
            'common_name_match': [],
            'elliptic_curves': [],
            'enable': False,
            'enhance': False,
            'send_close_alerts': True,
            'server_name': False,
            'session_cache_enabled': 'use_default',
            'session_tickets_enabled': 'use_default',
            'signature_algorithms': '',
            'strict_verify': False,
            'support_ssl3': 'use_default',
            'support_tls1': 'use_default',
            'support_tls1_1': 'use_default',
            'support_tls1_2': 'use_default'
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': '',
            'response_timeout': 0
        }
    }
}

drain_node = {
    'properties': {
        'auto_scaling': {
            'addnode_delaytime': 0,
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'securitygroupids': [],
            'size_id': '',
            'subnetids': []
        },
        'basic': {
            'bandwidth_class': '',
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': ['Ping'],
            'node_close_with_rst': False,
            'node_connection_attempts': 3,
            'node_delete_behavior': 'immediate',
            'node_drain_to_delete_timeout': 0,
            'nodes_table': [
                {
                    'node': '10.0.0.1:8000',
                    'state': 'draining',
                    'priority': 1,
                    'weight': 1
                }
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'dns_autoscale': {
            'enabled': False,
            'hostnames': [],
            'port': 80
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'kerberos_protocol_transition': {
            'principal': '',
            'target': ''
        },
        'l4accel': {
            'snat': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'priority_enabled': False,
            'priority_nodes': 1
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'service_discovery': {
            'enabled': False,
            'interval': 10,
            'plugin': '',
            'plugin_args': '',
            'timeout': 0
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'cipher_suites': '',
            'client_auth': False,
            'common_name_match': [],
            'elliptic_curves': [],
            'enable': False,
            'enhance': False,
            'send_close_alerts': True,
            'server_name': False,
            'session_cache_enabled': 'use_default',
            'session_tickets_enabled': 'use_default',
            'signature_algorithms': '',
            'strict_verify': False,
            'support_ssl3': 'use_default',
            'support_tls1': 'use_default',
            'support_tls1_1': 'use_default',
            'support_tls1_2': 'use_default'
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': '',
            'response_timeout': 0
        }
    }
}

disable_node = {
    'properties': {
        'auto_scaling': {
            'addnode_delaytime': 0,
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'securitygroupids': [],
            'size_id': '',
            'subnetids': []
        },
        'basic': {
            'bandwidth_class': '',
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': ['Ping'],
            'node_close_with_rst': False,
            'node_connection_attempts': 3,
            'node_delete_behavior': 'immediate',
            'node_drain_to_delete_timeout': 0,
            'nodes_table': [
                {
                    'node': '10.0.0.1:8000',
                    'state': 'disabled',
                    'priority': 1,
                    'weight': 1
                }
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'dns_autoscale': {
            'enabled': False,
            'hostnames': [],
            'port': 80
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'kerberos_protocol_transition': {
            'principal': '',
            'target': ''
        },
        'l4accel': {
            'snat': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'priority_enabled': False,
            'priority_nodes': 1
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'service_discovery': {
            'enabled': False,
            'interval': 10,
            'plugin': '',
            'plugin_args': '',
            'timeout': 0
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'cipher_suites': '',
            'client_auth': False,
            'common_name_match': [],
            'elliptic_curves': [],
            'enable': False,
            'enhance': False,
            'send_close_alerts': True,
            'server_name': False,
            'session_cache_enabled': 'use_default',
            'session_tickets_enabled': 'use_default',
            'signature_algorithms': '',
            'strict_verify': False,
            'support_ssl3': 'use_default',
            'support_tls1': 'use_default',
            'support_tls1_1': 'use_default',
            'support_tls1_2': 'use_default'
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': '',
            'response_timeout': 0
        }
    }
}

pool_status = {
    'statistics': {
        'algorithm': 'roundrobin',
        'bw_limit_bytes_drop': 0,
        'bw_limit_pkts_drop': 0,
        'bytes_in': 0,
        'bytes_out': 0,
        'conns_queued': 0,
        'disabled': 0,
        'draining': 0,
        'max_queue_time': 0,
        'mean_queue_time': 0,
        'min_queue_time': 0,
        'nodes': 1,
        'persistence': 'none',
        'queue_timeouts': 0,
        'session_migrated': 0,
        'state': 'active',
        'total_conn': 0
    }
}

nodes_status = {
    'statistics': {
        'current_conn': 0,
        'current_requests': 0,
        'errors': 0,
        'failures': 0,
        'new_conn': 0,
        'pooled_conn': 0,
        'port': 8000,
        'response_max': 0,
        'response_mean': 0,
        'response_min': 0,
        'state': 'alive',
        'total_conn': 0
    }
}

get_pool_old = {
    'properties': {
        'auto_scaling': {
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'size_id': ''
        },
        'basic': {
            'bandwidth_class': '',
            'disabled': [],
            'draining': [],
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': [
                'Ping'
            ],
            'node_connection_attempts': 3,
            'nodes': [
                '10.0.0.1:8000',
                '10.0.0.2:8000'
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'node_weighting': [
                {
                    'node': '10.0.0.1:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.2:8000',
                    'weight': 1
                }
            ],
            'priority_enabled': False,
            'priority_nodes': 1,
            'priority_values': []
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'client_auth': False,
            'enable': False,
            'enhance': False,
            'send_close_alerts': False,
            'server_name': False,
            'strict_verify': False
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': ''
        }
    }
}

get_pool_add_old = {
    'properties': {
        'auto_scaling': {
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'size_id': ''
        },
        'basic': {
            'bandwidth_class': '',
            'disabled': [],
            'draining': [],
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': [
                'Ping'
            ],
            'node_connection_attempts': 3,
            'nodes': [
                '10.0.0.1:8000',
                '10.0.0.2:8000',
                '10.0.0.3:8000'
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'node_weighting': [
                {
                    'node': '10.0.0.1:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.2:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.3:8000',
                    'weight': 1
                }
            ],
            'priority_enabled': False,
            'priority_nodes': 1,
            'priority_values': []
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'client_auth': False,
            'enable': False,
            'enhance': False,
            'send_close_alerts': False,
            'server_name': False,
            'strict_verify': False
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': ''
        }
    }
}

drain_node_old = {
    'properties': {
        'auto_scaling': {
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'size_id': ''
        },
        'basic': {
            'bandwidth_class': '',
            'disabled': [],
            'draining': [
                '10.0.0.1:8000'
            ],
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': [
                'Ping'
            ],
            'node_connection_attempts': 3,
            'nodes': [
                '10.0.0.2:8000',
                '10.0.0.3:8000'
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'node_weighting': [
                {
                    'node': '10.0.0.1:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.2:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.3:8000',
                    'weight': 1
                }
            ],
            'priority_enabled': False,
            'priority_nodes': 1,
            'priority_values': []
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'client_auth': False,
            'enable': False,
            'enhance': False,
            'send_close_alerts': False,
            'server_name': False,
            'strict_verify': False
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': ''
        }
    }
}

disable_node_old = {
    'properties': {
        'auto_scaling': {
            'cloud_credentials': '',
            'cluster': '',
            'data_center': '',
            'data_store': '',
            'enabled': False,
            'external': True,
            'hysteresis': 20,
            'imageid': '',
            'ips_to_use': 'publicips',
            'last_node_idle_time': 3600,
            'max_nodes': 4,
            'min_nodes': 1,
            'name': '',
            'port': 80,
            'refractory': 180,
            'response_time': 1000,
            'scale_down_level': 95,
            'scale_up_level': 40,
            'size_id': ''
        },
        'basic': {
            'bandwidth_class': '',
            'disabled': [
                '10.0.0.1:8000'
            ],
            'draining': [],
            'failure_pool': '',
            'max_connection_attempts': 0,
            'max_idle_connections_pernode': 50,
            'max_timed_out_connection_attempts': 2,
            'monitors': [
                'Ping'
            ],
            'node_connection_attempts': 3,
            'nodes': [
                '10.0.0.2:8000',
                '10.0.0.3:8000'
            ],
            'note': '',
            'passive_monitoring': True,
            'persistence_class': '',
            'transparent': False
        },
        'connection': {
            'max_connect_time': 4,
            'max_connections_per_node': 0,
            'max_queue_size': 0,
            'max_reply_time': 30,
            'queue_timeout': 10
        },
        'ftp': {
            'support_rfc_2428': False
        },
        'http': {
            'keepalive': True,
            'keepalive_non_idempotent': False
        },
        'load_balancing': {
            'algorithm': 'round_robin',
            'node_weighting': [
                {
                    'node': '10.0.0.1:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.2:8000',
                    'weight': 1
                },
                {
                    'node': '10.0.0.3:8000',
                    'weight': 1
                }
            ],
            'priority_enabled': False,
            'priority_nodes': 1,
            'priority_values': []
        },
        'node': {
            'close_on_death': False,
            'retry_fail_time': 60
        },
        'smtp': {
            'send_starttls': True
        },
        'ssl': {
            'client_auth': False,
            'enable': False,
            'enhance': False,
            'send_close_alerts': False,
            'server_name': False,
            'strict_verify': False
        },
        'tcp': {
            'nagle': True
        },
        'udp': {
            'accept_from': 'dest_only',
            'accept_from_mask': ''
        }
    }
}
