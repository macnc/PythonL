#!/usr/bin/python
# _*_coding: utf-8

import os
import unittest

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input('>')

if door == "1":
    print "There is a giant bear here eating a cheese. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input('>')

    if bear == "1":
        print "The bear eats you face off. Good job!"
    elif bear == "2":
        print "The bear eats you legs off. Good job!"
    else:
        print "Well, doing %d is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina"
    print "1. Bluebarries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding resolvers yelling melodies"

    insanity = raw_input('>')

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job."
    else:
        print "The insanity rote your eyes into a pool of musk. Good job."

else:
    print "You stumple around and fall on a knife and die. Good job"
