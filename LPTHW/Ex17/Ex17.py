#!/use/bin
# _*_coding: utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Okay, Let's copy data from %s to %s" % (from_file, to_file)
print "Job's processing..."
print

# We can do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit the Enter to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "OK! All jobs done!"
out_file.close()
in_file.close()