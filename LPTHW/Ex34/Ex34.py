#!/usr/bin/python
# _*_coding: utf-8

'''
How to access elements of Lists?
I will create a function which accept arguments and return the result from function.
 '''

import os

animals = ['bear', 'tiger', 'penguin', 'zebra']

def what_animals(index):
    if index in range(0, len(animals)):
        print 'Your answer is: ' + animals[index]
    else:
        print 'There are no animals like this here!'

which = int(raw_input('Which one in animals do you want to know? >'))
what_animals(which)