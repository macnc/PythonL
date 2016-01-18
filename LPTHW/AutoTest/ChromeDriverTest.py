#!/usr/bin/python
# _*_coding: utf-8

import time
from selenium import webdriver

path = '/Library/Selenium/chromedriver'
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get('http://www.google.com/xhtml')
time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('Google Test Technology')
search_box.submit()

time.sleep(5)
driver.quit()
