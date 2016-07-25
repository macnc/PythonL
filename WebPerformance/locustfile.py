#!/usr/local/bin/python
# _*_coding: utf-8

from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):
	@task
	def my_task(self):
		print "The my_task function in class My_Tesk_Set."
		
		
class MyLocust(Locust):
	task_set = MyTaskSet
	min_wait = 5000
	max_wait = 15000