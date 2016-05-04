#! /usr/local/bin/python
# _*_coding: utf-8


charset = 'abcdefghijklmnopqrstuvwxyz' * 3
for i in range(0, len(charset)/2):
        print charset[len(charset)-1-i:i:-1]
