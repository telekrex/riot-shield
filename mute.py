#!/usr/bin/env python3
import sys
from platform import system
hosts = 'C:\\Windows\\System32\\drivers\\etc\\hosts' if system() == 'Windows' else '/etc/hosts'
try:
    if str(sys.argv[1]) in ['active', 'activate', 'enable', 'enabled', 'start', 'go', 'on']:
        target = 'hosts muted'
        print('Enabling hosts muted')
    else:
        target = 'hosts default'
        print('Resetting hosts to default')
    with open(target, 'r') as file:
        contents = file.read()
    with open(hosts, 'w') as file:
        file.write(contents)
    print('Hosts contents updated')
except:
    print('Invalid arguments')
