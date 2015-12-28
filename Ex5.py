#!/usr/bin/
# _*_coding: utf-8

my_name = "suntao"
my_hight = 1.85
my_age = 33
my_weight = 159
my_teeth = "White"
my_hair = "Black"
my_eye = "blue"

print "Let's talk about %s" % my_name
print "He's %d inches tall" % my_hight
print "He's %d pounds heavy" % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (my_eye, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and, %d, I get %d." % (my_age, my_hight, my_weight, my_age + my_hight + my_weight)