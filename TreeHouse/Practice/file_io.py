#!/usr/local/bin/python3
# _*_coding: utf-8

import sys


def remember(thing):
    with open('test.txt', 'a') as file:
        file.write(thing + '\n')


def show():
    # open a file and list all of content in it.
    with open('test.txt', 'r') as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(''.join(sys.argv[1:]))