#!/usr/bin/python
#VOA Special English MP3 Downloader.
#Written by Timothy 2010.3.10
import urllib,time
from xml.dom import minidom
from os import system


url = "http://www1.voanews.com/templates/Articles.rss?sectionPath=/learningenglish/home"
link = urllib.urlopen(url)
# content=link.read()
rss = minidom.parse(link)
elements = rss.getElementsByTagName('media:content')
for element in elements:
    if element.hasAttribute('type'):
        print 'Now downloading:' + element.getAttribute('url')
        system('wget -nc  ' + element.getAttribute('url'))
