#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-


# Let's set up some customized function for doing math.
# These functions will be return the result.
# define add function
def add(a, b):
    """
    The function for do additions.
    """
    print "ADDING %d + %d" % (a, b)
    return a + b


# define subtract function
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


# define multiply function
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


# define divide function
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


# do some math by calling functions.
print "Let's do some math with just functions!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print out the result of calculation.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % \
    (age, height, weight, iq)

# A puzzle for the extract credit, type it in anyway.
print "Here is a puzzle."
# set up a formula by calling functions
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print out a meessage with result embadded.
print "That becomes: ", what, "Can you do it by hand?"

# let's make my own formula with functions.
# how to make this formula(24 + 34 / 100 - 1023) with functions?
mine = multiply(add(24, divide(34, 100)), 1023)
print "24 + 34 / 100 - 1023 = ? | %d" % mine
