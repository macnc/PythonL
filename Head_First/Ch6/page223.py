#!/usr/local/bin/python3
# _*_coding: utf-8

# Code for page223

import os
import pickle
from athletelist import AthleteList


def get_coach_data(filename):
	# Not shown here as it has not changed since the last chapter
	
	
def put_to_store(file_list):
	all_athletes = {}
	for fl in file_list:
		ath = get_coach_data(fl)
		all_athletes[ath.name] = ath
		try:
			with open('athletes.pickle', 'wb') as athf:
				pickle.dump(all_athletes, athf)
	
	
	return(all_athletes)
	
	
def get_from_store():
	all_athletes = {}
	
	
	return(all_athletes)