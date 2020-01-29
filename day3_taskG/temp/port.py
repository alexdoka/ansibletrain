#! /usr/bin/env python
import psutil
#p = psutil.Process(6556)
#res = p.as_dict(attrs=['pid', 'name', 'username', 'connections'])

def print_port_process(pid):
    res_dict = {}
    p = psutil.Process(pid)
    res = p.as_dict(attrs=['pid', 'name', 'username', 'connections'])
    res_dict["pid"] = res['pid']
    res_dict["name"] = res['name']
    res_dict["username"] = res['username']
    res_dict["connections"] = res['connections']
    #.as_dict(attrs=['fd'])
    return res_dict

# print(print_port_process(8391))
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('127.0.0.1', 3306))

if result == 0:
    print('socket is open')
s.close()

print(1)
