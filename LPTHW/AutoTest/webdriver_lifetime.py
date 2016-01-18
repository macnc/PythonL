#!/usr/bin/python
# _*_coding: utf-8

import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('/Library/Selenium/chromedriver')
service.start()

capabilities = {'chrome.binary':'/Applications/Google Chrome.app'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml')
time.sleep(5)
driver.quit()