#!/usr/local/bin/python3
# _*_coding: utf-8


import fileinput


with fileinput.input() as f_input:
	for line in f_input:
		print(line, end='')