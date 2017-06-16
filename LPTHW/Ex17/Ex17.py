#!/usr/local/Cellar/python/2.7.13/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

# we accept three arguments in this script.
script, from_file, to_file = argv

# start the workflow.
print "Copying from %s to %s" % (from_file, to_file)

# set up a file object for storing file data.
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# calculate the size of file for copying, and then print it out.
print "The input file is %d bytes long." % len(indata)

# check out the from_file exists or not, and then print the
# the result out.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abord/."
# only accept RETURN and CTRL-C ?
# what if I hit other keys?
raw_input()

# set up another file object for storing copying target file.
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close the file stream.
out_file.close()
in_file.close()
