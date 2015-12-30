#!/usr/bin/
# _*_coding: utf-8

import os,sys

# 反斜杠是一个转换符，用于在字符串中添加特殊字符的一种转换形式。
tabby_cat = "\tI'm tabbed in."
persian_cat = "\tI'm split \non a line."
backslash_cat = "I'm \\ a \\ cat"

# \t就是一个tab缩进符
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

