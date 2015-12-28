#!/usr/bin/
# _*_coding: utf-8

import sys,os

# Here's new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months

# 我不太理解：这里的注释的东西为什么会被打印出来？难道是多行注释只要是在print函数之后，都会被打印出来
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or6.
"""
# 貌似单行不会被打印出来
print #我是一直都很爱你。