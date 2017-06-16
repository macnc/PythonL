#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blackslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

bad_ketty = '''
Hey I am niniwa, here are my rules:
\t* No smoking in the house
\t* No mass in the house
\t* Talk to me when I am available
\t* Give a bug hug when I am sad.
'''

print tabby_cat
print persian_cat
print blackslash_cat
print fat_cat
print bad_ketty
