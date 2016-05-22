#! /usr/local/bin/python3
# _*_coding: utf-8


import sys


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    '''
    This function is used to print out list data as wrapped text on command
    line, we will continue to make some modification for saving these
    information to the file as formatted text.
    '''

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fn)
                # Or I can with the code like this way.
                # print('\t'*level, end='')
                print(each_item, file=fn)
