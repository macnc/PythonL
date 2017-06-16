#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-


import ex25
import re

sentence = open('100west.txt').read()
words = ex25.break_words(sentence)


# Remove all of symbels from big string.
def remove_symbel_str(text):
    """Find all of the string word which contain special symbels."""
    pattern = r"""[.,:;!?\\]"""
    return re.sub(pattern, ' ', text).split()


# Remove all of '\n' elements from str words and list.
def clean_bk(wds):
    r"""Remove all of '\n' from the string word."""
    return [w.rstrip() for w in wds]


# Romove all of '' elements from string list.
def remove_black(wds):
    """Remove all of black elements from list"""
    return [w for w in wds if w != '']


# Select all of elements which contain '$' in it.
def dollars(wds):
    """Return all of words which contain '$' in it."""
    return [w for w in wds if '$' in w]


# Select all of number elements from list.
def select_numbers(wds):
    """Return all of words which contain numbers in it."""
    return [w for w in wds if w.isdigit()]


# Select all of elements which contain '$' and numbers in it.
def not_words(wds):
    """Return all of elements which is not word."""
    return dollars(wds) + select_numbers(wds)


# print select_numbers(remove_black(clean_bk(words)))
# print remove_dot(remove_black(clean_bk(words)))
# print remove_dot(remove_black(clean_bk(words)))
