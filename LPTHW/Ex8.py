#!/use/bin/
# _*_coding: utf-8

import sys,os

# 定义一个语句输入的格式器，后面会通过%加空格的方式连接多个值在Formatter中填充并以formatter中定义的格式显示出来。
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it doesn't sing.",
	"So I said good night."
)