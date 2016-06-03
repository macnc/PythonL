#!/usr/local/bin/python3
# _*_coding: utf-8

import sqlite3


c = sqlite3.connect("coachdata2.sqlite")
cursor = c.cursor()
cursor.execute('''create table athletes (
				id integer primary key autoincrement unique not null,
				name text not null,
				dob date not null)''')

cursor.execute('''create table timing_data (
				athlete_id integer not null,
				value text not null,
				foreign key (athlete_id) references athletes)''')
				

c.commit()
c.close()