#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-

from sys import argv

# accept arguments from system terminal parameter
script, filename = argv

# print out some tips and options for user
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

# accept input from standard IO
# accept two options for the next workflow.
raw_input("?")

# set up a file object for opening a file.
print "Opeing the file..."
target = open(filename, 'w')

# start for truncate the target file.
print "Truncating the file. Goodbye!"
target.truncate()

# print out some tips for content input from user.
print "Now I'm going to ask you for three lines."

# define three variables for accepting use's input.
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

# print out the tip message for start writing the content.
print "I'm going to write these to the file."

# writ2 the content to target file.
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

# close the file stream.
print "And finally, we close it."
print "✅ " * 20 + "\n"
target.close()

# print out the content of updated file.
print "Here is the file you updated with the current script:"
print "-" * 20
after_writen = open(filename, 'r')
print after_writen.read()
after_writen.close()
