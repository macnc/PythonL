#! /usr/bin/python
# _*_coding: utf-8

charset = 'abcdefghijklmnopqrstuvwxyz' * 2
for i in range(0, len(charset)):
    if i > len(charset)/2:
        break;
    else:
        print ' ' * i + charset[i:len(charset)-i]
