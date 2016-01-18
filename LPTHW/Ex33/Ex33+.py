#!/usr/bin/python
# _*_coding: utf-8

def test(times):
    i = 0
    numbers = []

    while i < times:
        print "At the top is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

time = input('How many times do you want to loop?')
print "Are you sure: ", time
myNumbers = test(time)

print myNumbers
