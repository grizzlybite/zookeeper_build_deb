#!/usr/bin/env python3

import os
import socket
import subprocess

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    check_port_result = sock.connect_ex((host , int(port) ))
    sock.close()
    return check_port_result

def check_health(host, port, word):
    cmd = 'echo {0} | nc -d3 {1} {2}'.format(word, host, port)
    health_check_result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    data = health_check_result.communicate()
    return str(data[0])

def check_service_stat(host, port, word):
    cmd = 'echo {0} | nc {1} {2}'.format(word, host, port)
    service_stat_check_result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    data = service_stat_check_result.communicate()
    for opt in data:
        if "standalone" and "Sent" in opt:
            return 0
        else:
            return 1
