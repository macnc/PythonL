#!/usr/bin/python/
# _*_coding: utf-8

import os,sys

people = 30
cars = 40
trucks= 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide."

if trucks < cars and cars > people:
    print "That's too many cars"
elif trucks > cars or car < people:
    print "Too many cars"
else:
    print "We still can't decide."

if people > trucks:
    print "Aliright Let's just take the trucks"
else:
    print "Fine, let's stay home then."
