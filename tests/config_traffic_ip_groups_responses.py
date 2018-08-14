traffic_ip_groups = {
    u'children': [
        {
            u'href': u'/api/tm/5.2/config/active/traffic_ip_groups/Default%20EIP',
            u'name': u'Default EIP'
        },
        {
            u'href': u'/api/tm/5.2/config/active/traffic_ip_groups/TLS%201.0%20Disabled',
            u'name': u'TLS 1.0 Disabled'
        },
        {
            u'href': u'/api/tm/5.2/config/active/traffic_ip_groups/www.example.com',
            u'name': u'www.example.com'
        },
    ]
}

traffic_ip_group = {
    u'properties': {
        u'basic': {
            u'backend_traffic_ips': [],
            u'enabled': True,
            u'hash_source_port': False,
            u'ip_assignment_mode': u'balanced',
            u'ip_mapping': [],
            u'ipaddresses': [
                u'192.168.100.1'
            ],
            u'keeptogether': False,
            u'location': 0,
            u'machines': [
                u'10.0.0.1'
            ],
            u'mode': u'ec2vpcelastic',
            u'multicast': u'',
            u'note': u'',
            u'rhi_bgp_metric_base': 10,
            u'rhi_bgp_passive_metric_offset': 10,
            u'rhi_ospfv2_metric_base': 10,
            u'rhi_ospfv2_passive_metric_offset': 10,
            u'rhi_protocols': u'ospf',
            u'slaves': []
        }
    }
}

traffic_ip_stats = {
    u'statistics': {
        u'state': u'lowered',
        u'time': 730457300
    }
}

traffic_managers = {
    u'children': [
        {
            u'href': u'/api/tm/5.2/config/active/traffic_managers/10.0.0.1',
            u'name': u'10.0.0.1'
        }
    ]
}
