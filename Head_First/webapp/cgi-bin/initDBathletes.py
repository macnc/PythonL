#!/usr/local/bin/python3
# _*_coding: utf-8

import sqlite3


connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

import glob
import athletemodel
data_files = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
	name = athletes[each_ath].name
	dob = athletes[each_ath].dob
	
	cursor.execute("insert into athletes (name, dob) values (?, ?)", (name, dob))
	connection.commit()
	
connection.close()	