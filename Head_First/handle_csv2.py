#! /usr/local/bin/python3
# _*_coding: utf-8


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
