#!/usr/local/bin/python
# _*_coding: utf-8

from locust import HttpLocust, TaskSet, task


class Performance(TaskSet):
	@task(1)
	def inventories(self):
		self.client.get('/api/stores/demostore/inventories')

	@task(1)
	def updates(self):
		self.client.get('/api/stores/demostore/updates/20160720114746000')


	@task(1)
	def heart_beat(self):
		self.client.get('/api/heartbeat.json?t=1469600402579')



class MenPuJi(HttpLocust):
	task_set = Performance
	host = "http://172.16.255.135:8000/"
	min_wait = 5000
	max_wait = 15000
