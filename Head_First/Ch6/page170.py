#!/usr/local/bin/python3

import os

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' +secs)


def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print("File error: " + str(ioerr))
		return(None)
		
james = get_coach_data('james.txt')		
print(sorted(set([sanitize(t) for t in james]))[0:3])

