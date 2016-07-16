#!/usr/local/bin/python
# _*_coding: utf-8


import re
import subprocess


def check_process(process):
    '''
    The defination of process checking
    '''
    returnprocess = False
    s = subprocess.Popen(["ps", "ax"],stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            returnprocess = True

    if returnprocess == False:
      print 'no process executing'
    if returnprocess == True:
      print 'process executing'

# Test the function
if __name__ == '__main__':
    check_process('jetty')
