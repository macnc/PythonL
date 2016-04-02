#! /usr/bin/python
# _*_coding: utf-8

import sys
import mystuff

# The Module style
mystuff.apple()
print mystuff.tangerine

# The class coding process
class MyStuff(object):
    def __init__(self):
        self.tangerine = 'And now a thousand years between'

    def apple(self):
        print "I AM CLASSY APPLES!"

# The class style
thing = MyStuff()
thing.apple()
print thing.tangerine

# The dict style
mystuff['apples']
