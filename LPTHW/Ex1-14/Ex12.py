#!/usr/bin/
# -*- coding: utf-8 -*-

name = raw_input("Name? ")
age = raw_input("How old are you?\n")
weight = raw_input("How much do you weight?\n")
height = raw_input("How tall are you?\n")

print "So, your name is %s, and you're %r years old, %r meters tall and %r \
    kgs heavy." % (name, int(age), int(height), int(weight))
