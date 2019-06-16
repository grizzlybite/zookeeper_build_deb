#!/usr/bin/env python3

import unittest
import socket
import subprocess



from smoke_func import check_port
from smoke_func import check_health
from smoke_func import check_service_stat

host = '127.0.0.1'
port = '2181'

class TestPort(unittest.TestCase):
    def test_port_available(self):
        """
        Test that port available
        """
        result = check_port(host, port)
        self.assertEqual(result,0) 

class TestServiceStatus(unittest.TestCase):
    def test_health_check(self):
        """
        Tests if server is running in a non-error state
        """
        word = 'ruok'
        result = check_health(host, port, word)
        self.assertEqual(result,'imok') 

class TestServiceStatistics(unittest.TestCase):
    def test_service_stat_check(self):
        """
        Tests if server show brief details of the server
        """
        word = 'stat'
        result = check_service_stat(host, port, word)
        self.assertEqual(result,0) 

if __name__ == '__main__':
    unittest.main()
