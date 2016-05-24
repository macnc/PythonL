# -*- coding: utf-8 -*-
"""
Created on Mon May 23 18:02:51 2016

@author: suntao
"""
i = 0

try:
    with open('sketch.txt') as data:
        for el in data:
            try:
            # if len(el.split(':', 1)) == 2:
                (r, ls) = el.split(':', 1)
                ls = ls.strip()
                i = i + 1
                print("#%d" % i, r, " ", ls)
            except ValueError:
                pass
except IOError as e:
    print('Error: ' + str(e))