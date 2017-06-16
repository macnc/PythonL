#! /usr/local/bin/python3
# _*_coding: utf-8

from os import system as sys


def create(list_num):
    for item in list_num:
        if isinstance(item, list) and not len(item):
            sys('mkdir %s' % item.__name__)
            create(item)
        elif isinstance(item, list) and not item:
            sys('mkdir %s' % item.__name__)
        else:
            sys('touch %s' % item)

    print('Here is your project structure.')
    sys('tree')

templates = ['404.html', '500.html', 'base.html', 'index.html', 'user.html']
static = []
main = ['__init__.py', 'errors.py', 'form.py', 'view.py']
app = [templates, static, main]
migrations = []
test = ['__init__.py', 'test.py']
venv = []
flasky = [app, migrations, test, venv, 'requirements.txt', 'config.py', 'manage.py']

# create(flasky)
