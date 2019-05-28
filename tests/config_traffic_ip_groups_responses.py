traffic_ip_groups = {
    'children': [
        {
            'href': '/api/tm/5.2/config/active/traffic_ip_groups/Default%20EIP',
            'name': 'Default EIP'
        },
        {
            'href': '/api/tm/5.2/config/active/traffic_ip_groups/TLS%201.0%20Disabled',
            'name': 'TLS 1.0 Disabled'
        },
        {
            'href': '/api/tm/5.2/config/active/traffic_ip_groups/www.example.com',
            'name': 'www.example.com'
        },
    ]
}

traffic_ip_group = {
    'properties': {
        'basic': {
            'backend_traffic_ips': [],
            'enabled': True,
            'hash_source_port': False,
            'ip_assignment_mode': 'balanced',
            'ip_mapping': [],
            'ipaddresses': [
                '192.168.100.1'
            ],
            'keeptogether': False,
            'location': 0,
            'machines': [
                '10.0.0.1'
            ],
            'mode': 'ec2vpcelastic',
            'multicast': '',
            'note': '',
            'rhi_bgp_metric_base': 10,
            'rhi_bgp_passive_metric_offset': 10,
            'rhi_ospfv2_metric_base': 10,
            'rhi_ospfv2_passive_metric_offset': 10,
            'rhi_protocols': 'ospf',
            'slaves': []
        }
    }
}

traffic_ip_stats = {
    'statistics': {
        'state': 'lowered',
        'time': 730457300
    }
}

traffic_managers = {
    'children': [
        {
            'href': '/api/tm/5.2/config/active/traffic_managers/10.0.0.1',
            'name': '10.0.0.1'
        }
    ]
}
