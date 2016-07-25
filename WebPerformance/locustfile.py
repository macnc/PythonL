#!/usr/local/bin/python
# _*_coding: utf-8

from locust import HttpLocust, TaskSet, task


class Performance(TaskSet):
	@task(5)
	def inventories(self):
		self.client.get('/api/stores/demostore/inventories')

	@task(5)
	def updates(self):
		self.client.get('/api/stores/demostore/updates/20160720114746000')


class MyLocust(HttpLocust):
	task_set = Performance
	host = "http://172.16.255.135:8000/"
	min_wait = 5000
	max_wait = 15000
