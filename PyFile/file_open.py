#! /usr/local/bin/python3
# _*_coding: utf-8

import io


def file_open(filename):
    try:
        fobj = open(filename, 'r')
        for eachline in fobj:
            print(eachline,)
        fobj.close()
    except IOError(e):
        print('file open error:', e)


f = input("Enter the file name: ")
file_open(f)
