#!/usr/local/bin/python3
# _*_coding: utf-8

import requests as rq
import time
from multiprocessing import Pool


r1 = 'http://172.16.255.135:9090/api/stores/demostore/updates/20160622{}'.format(int(time.time()))
r2 = 'http://172.16.255.135:9090/api/stores/demostore/inventories'
r3 = 'http://172.16.255.135:9090/api/heartbeat.json?t={}'.format(int(time.time()))


def test0(rn):
	counter = 0
	while True:
		tm = int(time.time())
		rt = rq.get(rn)
		print('No.%d --- ' % counter + str(tm) + ' --- ' + str(rt.json()))
		print('No.%d' % i + ' test')
		counter += 1


def test1(rn):
	rt = rq.get(rn)
	print(str(time.time()) + ' --- ' + str(rt.json()))


if __name__ == '__main__':
	with Pool(100) as p:
		p.map(test0, [r1, r3])
