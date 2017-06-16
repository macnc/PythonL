#!/usr/bin/
# -*- coding: utf-8 -*-

# Define a variable named x with a string embedded variable in it
x = "There are %d types of people." % 10

# A string variable named binary
binary = "binary"

# A string variable named do_not have variable initialized
do_not = "don't"

# A string variable embedded two variables in it.
y = "Those who know %s and those who %s." % (binary, do_not)

# print out x
print x
# print out y
print y

# print out a text line embedded string variable replaced by x
print "I said: %r" % x
# print out a text line embedded string variable replaced by y
print "I also said: '%s'" % y

# Define a bool variable named hilarious with False value.
hilarious = False

# Define a variable named joke_evalution with '%r' repalced formatter
joke_evalution = "Isn't that joke so funny? %r"

# print out the joke_evalution variable and repalced %r formatter with
# hilarious value
print joke_evalution % hilarious

# Define two variables with initialization value.
w = "This is the left side of..."
e = "a string with a right side."

# print out these two string variables with appending.
print w + e
