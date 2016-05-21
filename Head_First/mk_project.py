#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:11:09 2016

@author: mpjtest
"""

from os import system as sys


templates = {'tempaltes': ['400.html', '500.html', 'base.html', 'index.html', \
    'user.html']}
statics = {'statics': []}
main = {'main': ['__init__.py', 'errors.py', 'form.py', 'view.py']}
app = {'app': templates, 'statics': statics, 'main': main}
migrations = {'migrations': []}
test = {'test': ['__init__.py', 'test.py']}
venv = {'venv': []}
root = [app, migrations, test, venv, 'requirements.txt', 'config.py', \
    'manage.py']


def mk_things(args):
    for item in args:
        if isinstance(item, dict):
            for k, v in item:
                sys('mkdir %s' % k)
                sys('touch')