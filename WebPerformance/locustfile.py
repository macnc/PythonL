#!/usr/local/bin/python
# _*_coding: utf-8

from locust import HttpLocust, TaskSet, task
import time


class Performance(TaskSet):

#	@task(1)
#	def inventories(self):
#		self.client.get('/api/stores/demostore/inventories')

	@task(1)
	def updates(self):
		self.client.get('/api/stores/demostore/updates/20160811171949000')


	@task(1)
	def heart_beat(self):
		t = int(time.time())
		self.client.get('/api/heartbeat.json?t={}'.format(t))
		
	@task(5)
	def user_login(self):
		self.client.post('/api/terminal/login/new', {"account":"15029258413","password":"e10adc3949ba59abbe56e057f20f883e"})



class MenPuJi(HttpLocust):
	task_set = Performance
	host = "http://172.16.255.180:9090"
	min_wait = 2000
	max_wait = 5000
