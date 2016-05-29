#!/usr/local/bin/python3
# _*_coding: utf-8

# Code for page223

import os
import pickle
from athletelist import *


#def get_coach_data(filename):
#	# Not shown here as it has not changed since the last chapter
#	pass
	
def put_to_store(file_list):
	all_athletes = {}
	for fl in file_list:
		ath = get_coach_data(fl)
		all_athletes[ath.name] = ath
		try:
			with open('athletes.pickle', 'wb') as athf:
				pickle.dump(all_athletes, athf)
		except IOError as ioer:
			print("File Error (put_and_store): " + str(ioer))
	
	return(all_athletes)
	
	
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			pickle.load(athf)
	except IOError as ioer:
		print('File Error (get_from_store): ' + str(ioer))
	
	return(all_athletes)
