#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv


# a function for printing out all of the content from a file.
def print_all(f):
    print f.read()


# go back to the begaining position of the file.
def rewind(f):
    f.seek(0)


# print out a line number and a line of content from a file.
def print_a_line(line_count, f):
    print line_count, f.readline()


# set up a variable for storing the content from a file with file stream.
current_file = open(input_file)

# print out the whole file content from a file.
print "First let's print the whole file:\n"
print_all(current_file)

# the cursor back to the begaining position of the file.
print "Now let's rewind, kind of like a tape."
rewind(current_file)

# print out the first line of content with line number.
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

# print out the second line of content with line number.
current_line += 1
print_a_line(current_line, current_file)

# print out the third line of content with line number.
current_line += 1
print_a_line(current_line, current_file)
