#! /usr/bin/python
# _*_coding: utf-8

# Write_Files.py implement

import pycurl

# As long as the file is opened in binary mode, both Python 2 and Python 3
# can write response body to it without decoding.

with open('out.html', 'wb') as f:
	c = pycurl.Curl()
	c.setopt(c.URL, 'http://app.menpuji.com/pos/index.html')
	c.setopt(c.WRITEDATA, f)
	c.perform()
	c.close()

# Code ended.
