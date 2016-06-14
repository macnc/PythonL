#! /usr/local/bin/python3
# _*_coding: utf-8


from find_it import find_closest
from tm2secs2tm import time2secs, secs2time

def find_nearest_time(look_for, target_data):
	what = time2secs(look_for)
	where = 


row_data = {}
with open('PaceData.csv') as data:
	column_heading = data.readline().strip().split(',')
	column_heading.pop(0)

	for each_line in data:
		row = each_line.strip().split(',')
		row_label = row.pop(0)
		inner_dict = {}
		for i in range(len(column_heading)):
			inner_dict[row[i]] = column_heading[i]
		row_data[row_label] = inner_dict
