#!/usr/bin/
# _*_coding: utf-8

import sys

def add(a, b):
    print "ADDING %d and %d" % (a, b)
    return a + b

def substract(a, b):
    print "SUBSTRACTING %d and %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d and %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d and %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(20, 5)
height = substract(78, 3)
weight = multiply(90, 2)
iq = divide(100, 2)

print
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print

# A puzzle for the extra credit, type it in anyway.
print "Here is the puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand."
