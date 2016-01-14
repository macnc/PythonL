#!/usr/bin/python
# _*_coding:utf-8

from selenium import webdriver
import time

dr = webdriver.Safari()
# dr = webdriver.Chrome()
time.sleep(5)
print "Safari will be closed..."
dr.quit()
print "Safari has been closed!"
