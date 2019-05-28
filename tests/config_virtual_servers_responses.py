virtual_servers = {
    'children': [
        {
            'name': 'Virtual Server 1',
            'href': '/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%201'
        },
        {
            'name': 'Virtual Server 2',
            'href': '/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%202'
        },
        {
            'name': 'Virtual Server 3',
            'href': '/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%203'
        },
        {
            'name': 'Virtual Server 4',
            'href': '/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%204'
        }
    ]
}

virtual_servers_v1 = {
    'children': [
        {
            'name': 'Virtual Server 1',
            'href': '/api/tm/1.0/config/active/vservers/Virtual%20Server%201'
        },
        {
            'name': 'Virtual Server 2',
            'href': '/api/tm/1.0/config/active/vservers/Virtual%20Server%202'
        },
        {
            'name': 'Virtual Server 3',
            'href': '/api/tm/1.0/config/active/vservers/Virtual%20Server%203'
        },
        {
            'name': 'Virtual Server 4',
            'href': '/api/tm/1.0/config/active/vservers/Virtual%20Server%204'
        }
    ]
}

get_vs = {
    'properties': {
        'aptimizer': {
            'enabled': False,
            'profile': []
        },
        'auth': {
            'saml_idp': '',
            'saml_nameid_format': 'none',
            'saml_sp_acs_url': '',
            'saml_sp_entity_id': '',
            'saml_time_tolerance': 5,
            'session_cookie_attributes': 'HttpOnly; SameSite=Strict',
            'session_cookie_name': 'VS_SamlSP_Auth',
            'session_log_external_state': False,
            'session_timeout': 7200,
            'type': 'none',
            'verbose': False
        },
        'basic': {
            'bandwidth_class': '',
            'bypass_data_plane_acceleration': False,
            'completion_rules': [],
            'connect_timeout': 10,
            'enabled': True,
            'glb_services': [],
            'listen_on_any': True,
            'listen_on_hosts': [],
            'listen_on_traffic_ips': [],
            'max_concurrent_connections': 0,
            'note': '',
            'pool': 'Pool1',
            'port': 8000,
            'protection_class': '',
            'protocol': 'http',
            'proxy_protocol': False,
            'request_rules': [],
            'response_rules': [],
            'slm_class': '',
            'ssl_decrypt': False,
            'transparent': False
        },
        'connection': {
            'keepalive': True,
            'keepalive_timeout': 10,
            'max_client_buffer': 65536,
            'max_server_buffer': 65536,
            'max_transaction_duration': 0,
            'server_first_banner': '',
            'timeout': 40
        },
        'connection_errors': {
            'error_file': 'Default'
        },
        'cookie': {
            'domain': 'no_rewrite',
            'new_domain': '',
            'path_regex': '',
            'path_replace': '',
            'secure': 'no_modify'
        },
        'dns': {
            'edns_client_subnet': True,
            'edns_udpsize': 4096,
            'max_udpsize': 4096,
            'rrset_order': 'fixed',
            'verbose': False,
            'zones': []
        },
        'ftp': {
            'data_source_port': 0,
            'force_client_secure': True,
            'force_server_secure': True,
            'port_range_high': 0,
            'port_range_low': 0,
            'ssl_data': True
        },
        'gzip': {
            'compress_level': 1,
            'enabled': False,
            'etag_rewrite': 'wrap',
            'include_mime': [
                'text/html',
                'text/plain'
            ],
            'max_size': 10000000,
            'min_size': 1000,
            'no_size': True
        },
        'http': {
            'add_cluster_ip': True,
            'add_x_forwarded_for': False,
            'add_x_forwarded_proto': False,
            'autodetect_upgrade_headers': True,
            'chunk_overhead_forwarding': 'lazy',
            'location_regex': '',
            'location_replace': '',
            'location_rewrite': 'if_host_matches',
            'mime_default': 'text/plain',
            'mime_detect': False,
            'strip_x_forwarded_proto': False
        },
        'http2': {
            'connect_timeout': 0,
            'data_frame_size': 4096,
            'enabled': False,
            'header_table_size': 4096,
            'headers_index_blacklist': [],
            'headers_index_default': True,
            'headers_index_whitelist': [],
            'headers_size_limit': 262144,
            'idle_timeout_no_streams': 120,
            'idle_timeout_open_streams': 600,
            'max_concurrent_streams': 200,
            'max_frame_size': 16384,
            'max_header_padding': 0,
            'merge_cookie_headers': True,
            'stream_window_size': 65535
        },
        'kerberos_protocol_transition': {
            'enabled': False,
            'principal': '',
            'target': ''
        },
        'l4accel': {
            'rst_on_service_failure': False,
            'service_ip_snat': False,
            'state_sync': False,
            'tcp_msl': 8,
            'timeout': 1800,
            'udp_count_requests': False
        },
        'l4stateless': {},
        'log': {
            'client_connection_failures': False,
            'enabled': False,
            'filename': '%zeushome%/zxtm/log/%v.log',
            'format': '%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i"',
            'save_all': True,
            'server_connection_failures': False,
            'session_persistence_verbose': False,
            'ssl_failures': False,
            'ssl_resumption_failures': False
        },
        'recent_connections': {
            'enabled': True,
            'save_all': False
        },
        'request_tracing': {
            'enabled': False,
            'trace_io': False
        },
        'rtsp': {
            'streaming_port_range_high': 0,
            'streaming_port_range_low': 0,
            'streaming_timeout': 30
        },
        'sip': {
            'dangerous_requests': 'node',
            'follow_route': True,
            'max_connection_mem': 65536,
            'mode': 'sip_gateway',
            'rewrite_uri': False,
            'streaming_port_range_high': 0,
            'streaming_port_range_low': 0,
            'streaming_timeout': 60,
            'timeout_messages': True,
            'transaction_timeout': 30
        },
        'smtp': {
            'expect_starttls': True
        },
        'ssl': {
            'add_http_headers': False,
            'cipher_suites': '',
            'client_cert_cas': [],
            'client_cert_headers': 'none',
            'elliptic_curves': [],
            'honor_fallback_scsv': 'use_default',
            'issued_certs_never_expire': [],
            'issued_certs_never_expire_depth': 1,
            'ocsp_enable': False,
            'ocsp_issuers': [],
            'ocsp_max_response_age': 0,
            'ocsp_stapling': False,
            'ocsp_time_tolerance': 30,
            'ocsp_timeout': 10,
            'request_client_cert': 'dont_request',
            'send_close_alerts': True,
            'server_cert_alt_certificates': [],
            'server_cert_default': '',
            'server_cert_host_mapping': [],
            'session_cache_enabled': 'use_default',
            'session_tickets_enabled': 'use_default',
            'signature_algorithms': '',
            'support_ssl3': 'use_default',
            'support_tls1': 'use_default',
            'support_tls1_1': 'use_default',
            'support_tls1_2': 'use_default',
            'trust_magic': False
        },
        'syslog': {
            'enabled': False,
            'format': '%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i"',
            'ip_end_point': '',
            'msg_len_limit': 1024
        },
        'tcp': {
            'close_with_rst': False,
            'nagle': False,
            'proxy_close': False
        },
        'transaction_export': {
            'brief': False,
            'enabled': True,
            'hi_res': False,
            'http_header_blacklist': ['Authorization']
        },
        'udp': {
            'end_point_persistence': True,
            'port_smp': False,
            'response_datagrams_expected': 1,
            'timeout': 7,
            'udp_end_transaction': 'one_response'
        },
        'web_cache': {
            'control_out': '',
            'enabled': False,
            'error_page_time': 30,
            'max_time': 600,
            'refresh_time': 2
        }
    }
}

vs_stats = {
    'statistics': {
        'auth_saml_redirects': 0,
        'auth_saml_responses': 0,
        'auth_saml_responses_accepted': 0,
        'auth_saml_responses_rejected': 0,
        'auth_sessions_created': 0,
        'auth_sessions_rejected': 0,
        'auth_sessions_used': 0,
        'bw_limit_bytes_drop': 0,
        'bw_limit_pkts_drop': 0,
        'bytes_in': 0,
        'bytes_out': 0,
        'cert_status_requests': 0,
        'cert_status_responses': 0,
        'connect_timed_out': 0,
        'connection_errors': 0,
        'connection_failures': 0,
        'current_conn': 0,
        'data_timed_out': 0,
        'direct_replies': 0,
        'discard': 0,
        'gzip': 0,
        'gzip_bytes_saved': 0,
        'http_cache_hit_rate': 0,
        'http_cache_hits': 0,
        'http_cache_lookups': 0,
        'http_rewrite_cookie': 0,
        'http_rewrite_location': 0,
        'keepalive_timed_out': 0,
        'max_conn': 0,
        'max_duration_timed_out': 0,
        'pkts_in': 0,
        'pkts_out': 0,
        'port': 8000,
        'processing_timed_out': 0,
        'protocol': 'http',
        'sip_rejected_requests': 0,
        'sip_total_calls': 0,
        'ssl_cache_lookup': 0,
        'ssl_cache_miss': 0,
        'ssl_cache_rejected': 0,
        'ssl_cache_resumed': 0,
        'ssl_cache_saved': 0,
        'ssl_new_session': 0,
        'ssl_ticket_expired': 0,
        'ssl_ticket_issued': 0,
        'ssl_ticket_key_not_found': 0,
        'ssl_ticket_received': 0,
        'ssl_ticket_rejected': 0,
        'ssl_ticket_resumed': 0,
        'total_dgram': 0,
        'total_http1_requests': 0,
        'total_http2_requests': 0,
        'total_http_requests': 0,
        'total_requests': 0,
        'total_tcp_reset': 0,
        'total_udp_unreachables': 0,
        'udp_timed_out': 0
    }
}
