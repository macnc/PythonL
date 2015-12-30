#!/usr/bin
# _*_coding: utf-8

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print "[%d]: %s" % (line_count, f.readline())

current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Now let's remind, kind of like a tape."

rewind(current_file)
print "Let's print three lines:"

current_line = 1

# 原来书本需要我敲出的代码
"""
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
"""

# 我自己用来验证readlin()方法的循环语句
while current_line <= 20:
    print_a_line(current_line, current_file)
    current_line += 1

print "Test done!"