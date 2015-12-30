#!/usr/bin
# _*_coding: utf-8

import sys,os

# This one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# OK, that args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# This just take one argument
def print_one(arg1):
    print "arg1: %s" % (arg1)

# This one takes no argument
def print_none():
    print "I got nothing."

print_two("Zed", "Shaw")
print_two_again("SunTAO", "Tanjingjing")
print_one("First!")
print_none()

