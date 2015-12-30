#!/usr/bin/
# _*_coding: utf-8

from sys import argv

# 第一个Script参数具体是干嘛的?
script, filename = argv

# 将文件内容打开负值给txt
txt = open(filename)

# 分别打印出文件名称和文件内容, txt可能通过这种赋值的方式转化为一个文本文件对象,可以调用框架的read()方法
print "Here is your file %r:" % filename
print txt.read()

# Once again.
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()