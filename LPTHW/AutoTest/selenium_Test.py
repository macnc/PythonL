#!/usr/bin/python
# _*_coding:utf-8

from selenium import webdriver
import time

dr = webdriver.Safari()
# dr = webdriver.Firefox()
# dr = webdriver.Chrome('/Library/Selenium/chromedriver')

# Opera浏览器还是没有调通
# dr = webdriver.Opera()
dr.maximize_window()
dr.get('http://www.google.com/')
time.sleep(5)

search_box = dr.find_element_by_name('q')
search_box.send_keys('Junit Test with intelliJ IDE')
search_box.submit()
time.sleep(10)

print "Safari will be closed..."
dr.quit()
print "Safari has been closed!"
