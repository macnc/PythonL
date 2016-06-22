#!/usr/local/bin/python3
# _*_coding: utf-8

import requests as rq
import time


r1 = 'http://172.16.255.135:9090/api/stores/demostore/updates/20160622{}'.format(int(time.time()))
r2 = 'http://172.16.255.135:9090/api/stores/demostore/inventories'
r3 = 'http://172.16.255.135:9090/api/heartbeat.json?t={}'.format(int(time.time()))

def test(rn):
	i = 0
	while True:
		tm = int(time.time())
		rt = rq.get(rn)
		print('No.%d --- ' % i + str(tm) + ' --- ' + str(rt.json()))
#		print('No.%d' % i + ' test')
		i += 1

test(r1)