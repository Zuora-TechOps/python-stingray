virtual_servers = {
    u'children': [
        {
            u'name': u'Virtual Server 1',
            u'href': u'/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%201'
        },
        {
            u'name': u'Virtual Server 2',
            u'href': u'/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%202'
        },
        {
            u'name': u'Virtual Server 3',
            u'href': u'/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%203'
        },
        {
            u'name': u'Virtual Server 4',
            u'href': u'/api/tm/5.2/config/active/virtual_servers/Virtual%20Server%204'
        }
    ]
}

virtual_servers_v1 = {
    u'children': [
        {
            u'name': u'Virtual Server 1',
            u'href': u'/api/tm/1.0/config/active/vservers/Virtual%20Server%201'
        },
        {
            u'name': u'Virtual Server 2',
            u'href': u'/api/tm/1.0/config/active/vservers/Virtual%20Server%202'
        },
        {
            u'name': u'Virtual Server 3',
            u'href': u'/api/tm/1.0/config/active/vservers/Virtual%20Server%203'
        },
        {
            u'name': u'Virtual Server 4',
            u'href': u'/api/tm/1.0/config/active/vservers/Virtual%20Server%204'
        }
    ]
}

get_vs = {
    u'properties': {
        u'aptimizer': {
            u'enabled': False,
            u'profile': []
        },
        u'auth': {
            u'saml_idp': u'',
            u'saml_nameid_format': u'none',
            u'saml_sp_acs_url': u'',
            u'saml_sp_entity_id': u'',
            u'saml_time_tolerance': 5,
            u'session_cookie_attributes': u'HttpOnly; SameSite=Strict',
            u'session_cookie_name': u'VS_SamlSP_Auth',
            u'session_log_external_state': False,
            u'session_timeout': 7200,
            u'type': u'none',
            u'verbose': False
        },
        u'basic': {
            u'bandwidth_class': u'',
            u'bypass_data_plane_acceleration': False,
            u'completion_rules': [],
            u'connect_timeout': 10,
            u'enabled': True,
            u'glb_services': [],
            u'listen_on_any': True,
            u'listen_on_hosts': [],
            u'listen_on_traffic_ips': [],
            u'max_concurrent_connections': 0,
            u'note': u'',
            u'pool': u'Pool1',
            u'port': 8000,
            u'protection_class': u'',
            u'protocol': u'http',
            u'proxy_protocol': False,
            u'request_rules': [],
            u'response_rules': [],
            u'slm_class': u'',
            u'ssl_decrypt': False,
            u'transparent': False
        },
        u'connection': {
            u'keepalive': True,
            u'keepalive_timeout': 10,
            u'max_client_buffer': 65536,
            u'max_server_buffer': 65536,
            u'max_transaction_duration': 0,
            u'server_first_banner': u'',
            u'timeout': 40
        },
        u'connection_errors': {
            u'error_file': u'Default'
        },
        u'cookie': {
            u'domain': u'no_rewrite',
            u'new_domain': u'',
            u'path_regex': u'',
            u'path_replace': u'',
            u'secure': u'no_modify'
        },
        u'dns': {
            u'edns_client_subnet': True,
            u'edns_udpsize': 4096,
            u'max_udpsize': 4096,
            u'rrset_order': u'fixed',
            u'verbose': False,
            u'zones': []
        },
        u'ftp': {
            u'data_source_port': 0,
            u'force_client_secure': True,
            u'force_server_secure': True,
            u'port_range_high': 0,
            u'port_range_low': 0,
            u'ssl_data': True
        },
        u'gzip': {
            u'compress_level': 1,
            u'enabled': False,
            u'etag_rewrite': u'wrap',
            u'include_mime': [
                u'text/html',
                u'text/plain'
            ],
            u'max_size': 10000000,
            u'min_size': 1000,
            u'no_size': True
        },
        u'http': {
            u'add_cluster_ip': True,
            u'add_x_forwarded_for': False,
            u'add_x_forwarded_proto': False,
            u'autodetect_upgrade_headers': True,
            u'chunk_overhead_forwarding': u'lazy',
            u'location_regex': u'',
            u'location_replace': u'',
            u'location_rewrite': u'if_host_matches',
            u'mime_default': u'text/plain',
            u'mime_detect': False,
            u'strip_x_forwarded_proto': False
        },
        u'http2': {
            u'connect_timeout': 0,
            u'data_frame_size': 4096,
            u'enabled': False,
            u'header_table_size': 4096,
            u'headers_index_blacklist': [],
            u'headers_index_default': True,
            u'headers_index_whitelist': [],
            u'headers_size_limit': 262144,
            u'idle_timeout_no_streams': 120,
            u'idle_timeout_open_streams': 600,
            u'max_concurrent_streams': 200,
            u'max_frame_size': 16384,
            u'max_header_padding': 0,
            u'merge_cookie_headers': True,
            u'stream_window_size': 65535
        },
        u'kerberos_protocol_transition': {
            u'enabled': False,
            u'principal': u'',
            u'target': u''
        },
        u'l4accel': {
            u'rst_on_service_failure': False,
            u'service_ip_snat': False,
            u'state_sync': False,
            u'tcp_msl': 8,
            u'timeout': 1800,
            u'udp_count_requests': False
        },
        u'l4stateless': {},
        u'log': {
            u'client_connection_failures': False,
            u'enabled': False,
            u'filename': u'%zeushome%/zxtm/log/%v.log',
            u'format': u'%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i"',
            u'save_all': True,
            u'server_connection_failures': False,
            u'session_persistence_verbose': False,
            u'ssl_failures': False,
            u'ssl_resumption_failures': False
        },
        u'recent_connections': {
            u'enabled': True,
            u'save_all': False
        },
        u'request_tracing': {
            u'enabled': False,
            u'trace_io': False
        },
        u'rtsp': {
            u'streaming_port_range_high': 0,
            u'streaming_port_range_low': 0,
            u'streaming_timeout': 30
        },
        u'sip': {
            u'dangerous_requests': u'node',
            u'follow_route': True,
            u'max_connection_mem': 65536,
            u'mode': u'sip_gateway',
            u'rewrite_uri': False,
            u'streaming_port_range_high': 0,
            u'streaming_port_range_low': 0,
            u'streaming_timeout': 60,
            u'timeout_messages': True,
            u'transaction_timeout': 30
        },
        u'smtp': {
            u'expect_starttls': True
        },
        u'ssl': {
            u'add_http_headers': False,
            u'cipher_suites': u'',
            u'client_cert_cas': [],
            u'client_cert_headers': u'none',
            u'elliptic_curves': [],
            u'honor_fallback_scsv': u'use_default',
            u'issued_certs_never_expire': [],
            u'issued_certs_never_expire_depth': 1,
            u'ocsp_enable': False,
            u'ocsp_issuers': [],
            u'ocsp_max_response_age': 0,
            u'ocsp_stapling': False,
            u'ocsp_time_tolerance': 30,
            u'ocsp_timeout': 10,
            u'request_client_cert': u'dont_request',
            u'send_close_alerts': True,
            u'server_cert_alt_certificates': [],
            u'server_cert_default': u'',
            u'server_cert_host_mapping': [],
            u'session_cache_enabled': u'use_default',
            u'session_tickets_enabled': u'use_default',
            u'signature_algorithms': u'',
            u'support_ssl3': u'use_default',
            u'support_tls1': u'use_default',
            u'support_tls1_1': u'use_default',
            u'support_tls1_2': u'use_default',
            u'trust_magic': False
        },
        u'syslog': {
            u'enabled': False,
            u'format': u'%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i"',
            u'ip_end_point': u'',
            u'msg_len_limit': 1024
        },
        u'tcp': {
            u'close_with_rst': False,
            u'nagle': False,
            u'proxy_close': False
        },
        u'transaction_export': {
            u'brief': False,
            u'enabled': True,
            u'hi_res': False,
            u'http_header_blacklist': [u'Authorization']
        },
        u'udp': {
            u'end_point_persistence': True,
            u'port_smp': False,
            u'response_datagrams_expected': 1,
            u'timeout': 7,
            u'udp_end_transaction': u'one_response'
        },
        u'web_cache': {
            u'control_out': u'',
            u'enabled': False,
            u'error_page_time': 30,
            u'max_time': 600,
            u'refresh_time': 2
        }
    }
}

vs_stats = {
    u'statistics': {
        u'auth_saml_redirects': 0,
        u'auth_saml_responses': 0,
        u'auth_saml_responses_accepted': 0,
        u'auth_saml_responses_rejected': 0,
        u'auth_sessions_created': 0,
        u'auth_sessions_rejected': 0,
        u'auth_sessions_used': 0,
        u'bw_limit_bytes_drop': 0,
        u'bw_limit_pkts_drop': 0,
        u'bytes_in': 0,
        u'bytes_out': 0,
        u'cert_status_requests': 0,
        u'cert_status_responses': 0,
        u'connect_timed_out': 0,
        u'connection_errors': 0,
        u'connection_failures': 0,
        u'current_conn': 0,
        u'data_timed_out': 0,
        u'direct_replies': 0,
        u'discard': 0,
        u'gzip': 0,
        u'gzip_bytes_saved': 0,
        u'http_cache_hit_rate': 0,
        u'http_cache_hits': 0,
        u'http_cache_lookups': 0,
        u'http_rewrite_cookie': 0,
        u'http_rewrite_location': 0,
        u'keepalive_timed_out': 0,
        u'max_conn': 0,
        u'max_duration_timed_out': 0,
        u'pkts_in': 0,
        u'pkts_out': 0,
        u'port': 8000,
        u'processing_timed_out': 0,
        u'protocol': u'http',
        u'sip_rejected_requests': 0,
        u'sip_total_calls': 0,
        u'ssl_cache_lookup': 0,
        u'ssl_cache_miss': 0,
        u'ssl_cache_rejected': 0,
        u'ssl_cache_resumed': 0,
        u'ssl_cache_saved': 0,
        u'ssl_new_session': 0,
        u'ssl_ticket_expired': 0,
        u'ssl_ticket_issued': 0,
        u'ssl_ticket_key_not_found': 0,
        u'ssl_ticket_received': 0,
        u'ssl_ticket_rejected': 0,
        u'ssl_ticket_resumed': 0,
        u'total_dgram': 0,
        u'total_http1_requests': 0,
        u'total_http2_requests': 0,
        u'total_http_requests': 0,
        u'total_requests': 0,
        u'total_tcp_reset': 0,
        u'total_udp_unreachables': 0,
        u'udp_timed_out': 0
    }
}
