#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-


# define a function for accepting two arguments.
# this function will print out some imformation about arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


def make_addition(arg1, arg2):
    '''
    This function is used for making addition math and then return the result.
    The result of the function are numbers type.
    '''
    print "This function will make addition math and return the result:"
    print "The result for addition math is %r." % (arg1 + arg2)


# The 1st senario for calling chhese_and_crackers.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# The 2nd senario for calling cheese_and_crackers with numbers parameters.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# The 3rd senario for calling cheese_and_crackers with numbers math \
# calculation as parameters.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# The 4th senario for calling cheese_and_crackers with variables math
# calculation as parameters.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# try self-made function for calling.
make_addition(22, 89)
