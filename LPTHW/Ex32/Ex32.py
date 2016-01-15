#!/usr/bin/python
# _*_coding: utf-8

import sys

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d number" % number

# Same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through a mix lists too
# notice we have to use %r since we don't know what's in it.
for i in change:
    print "I got %r" % i

# we can also create a list too, first start with an empty one
elements = []
# we can assign the list to a return value from a  range function
elements = range(-8, 0)
# then use the range function to do 0 to 6 counts
for i in range(0, 6):
    print "Add %d to the list." % i
    # append is a function that list understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print "Elements was: %d" % i

print "Finally the elements is:\n", elements
