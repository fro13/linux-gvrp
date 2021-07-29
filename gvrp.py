#!/usr/bin/env python3

import re
from netmiko import ConnectHandler

somehost = {
    "device_type": "linux",
    "host": "somehost.example.com",
    "port": "22",
    "username": "admin",
    "password": "passwd123"
}

with ConnectHandler(**somehost) as net_connect:
    output = net_connect.send_command('ip -br a') # or 'ip -br a | grep -o "vlan[0-9]\+"'
    result = re.finditer(r'vlan\d+', output)
    for i in result:
        output = net_connect.send_command(f'sudo ip link set dev {i.group()} type vlan gvrp on')
        print(net_connect.send_command(f'ip -detail link show dev {i.group()}'))