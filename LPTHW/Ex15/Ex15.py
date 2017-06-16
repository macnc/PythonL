#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-


# Inclue the fuction argv for argument accept from stand terminal
from sys import argv

# script name and file name will inputed from terminal
script, filename = argv
# Sep up a variable for open the file. Actually it's a file object
txt = open(filename)

# print out the file name you need to open.
print "Here's your file %r:" % filename
# print out the cotent of the file.
print txt.read()
txt.close()

# print out a open file tip message
print "Type the filename again:"
# accept a filename from prompt input
file_again = raw_input("> ")
# set up another variable for open this file.
txt_again = open(file_again)
# print out the content of another file.
print txt_again.read()
txt_again.close()
