#! /usr/bin/python
# _*_coding: utf-8

import pycurl

c = pycurl.Curl()
# Redirects to https://www.python.org/.
c.setopt(c.URL, 'http://app.menpuji.com/pos/index.html')

# Follow Redirects
c.setopt(c.FOLLOWLOCATION, True)
c.perform()
c.close()
