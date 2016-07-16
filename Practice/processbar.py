#!/usr/bin/python3
# _*_coding: utf-8


import time
import sys

toolbar_width = 40

# Setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
# return to start of line, after '['
sys.stdout.write("\b" * (toolbar_width + 1))

for i in xrange(toolbar_width):
    time.sleep(0.1)
    # Update the toolbar here
    sys.stdout.write("+")
    sys.stdout.flush()

sys.stdout.write("\n")
