#! /usr/bin/python
# _*_coding: utf-8

import os

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_body = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They really around the family",
                        "With pocket full of shells"])

my_song = Song(["我来到你的城市,", "你却不请我饭吃。", "你真是个吝啬鬼！"])
print "*" * 10 + "Here we go!" + "*" * 10
print "The 1st Song:"
print "-" * 50
happy_body.sing_me_a_song()
print
print

print "The 2nd Song:"
print "-" * 50
bulls_on_parade.sing_me_a_song()

print "The 3rd Song:"
print "-" * 50
my_song.sing_me_a_song()
