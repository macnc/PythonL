#!/usr/local/bin/python3
# _*_coding: utf-8

import os
import glob

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
		templ = data.strip().split(',')
		return(
			{'Name': templ.pop(0),
			'Dob': templ.pop(0),
			'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])
			}
		)
	except IOError as ioerr:
		print("File error: " + str(ioerr))
		return(None)

# Scan the 2gn sub-folder for list all of txt file as a list data type
#files = []
os.chdir("2gn/")
#for file in glob.glob("*.txt"):
#	files.append(file)

# Iteraling all of these files for making sporter's data
for item in glob.glob("*.txt"):
	people = get_coach_data(item)
	print(people['Name'] + "'s fastest time are:" + people['Times'])
	
	
	
	
