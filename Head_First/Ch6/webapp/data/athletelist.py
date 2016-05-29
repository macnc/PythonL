#!/usr/local/bin/python3
# _*_coding: utf-8

import os
import sys


# 将运动员的基本信息封装为一个运动员对象，做list内置对象的一个派生类；
# 该类继承了list的所有属性和方法
class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
		
	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])


# 清晰数据的函数, 统一将计时数据格式化为小数字符串
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' +secs)


# 从txt文件中，把相关文件中的数据转化为数据列表
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp = data.strip().split(',')
		return(AthleteList(temp.pop(0), temp.pop(0), temp))
	except IOError as e:
		print("Error: " + str(e))