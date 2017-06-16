#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 打印一行标题文字并以冒号结束。
print "I wil now count my chikens:"

# 打印母鸡的数量，开头以母鸡英文单词字符串开始，后面拼接计算出来的数字
print "Hens", 25 + 30 / 6
# 打印公鸡的数量，开头以公鸡英文单词字符串开始，后面拼接计算出来的数字
print "Roosters", 100 - 25 * 3 % 4

# 打印第二行标题文字，并以冒号结束
print "Now I will count the eggs:"

# 打印一个计算表达式的结果，计算表达式计算完毕之后由print函数打印出结果
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# 打印出来一个问题字符串，其中包含有数字计算表达式
print "Is it true that 3 + 2 < 5 - 7?"

# 打印出上一行字符串中含有数学表达式的计算结果
print 3 + 2 < 5 - 7

# 打印一个加法数学问题表达式的问题，后面拼接这个表达式的计算结果
print "What is 3 + 2?", 3 + 2
# 打印一个减法数学问题表达式的问题，后面拼接这个表达式的计算结果
print "What is 5 - 7?", 5 - 7

# 打印一行文字
print "Oh, that's why it's False."

# 打印另外一行文字
print "How about some more."

# 打印一个大于比较的逻辑表达式问题，后面拼接打印这个逻辑表达式的计算结果
print "Is it greater?", 5 > -2
# 打印一个大于等于的逻辑表达式问题，后面拼接打印这个逻辑表达式的计算结果
print "Is it greater or equal?", 5 >= -2
# 打印一个小于等于的逻辑表达式问题，后面拼接打印这个逻辑表达式的计算结果
print "Is it less or equal?", 5 <= -2

# Even though Python no need to declear the data type, but you
# still need initialize them for the type, or you can not get
# the right result from the math expression.
print "What is 4 / 7?", 4 / 7
print "Seems like we got the wrong result."

# If you want the math expression more accurate, you need
# floating point after the int numbers.
print "Something more complex? Okay, here we go:",
print "You need type the math expression like this: 7.0 / 4.0"
print "Now we can get the right result:", 7.0 / 4.0
