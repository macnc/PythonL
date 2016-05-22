#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:11:09 2016

@author: 孙涛
本文件的目的是要写一个程序来创建一个模板结构的文件夹，这个文件夹中嵌套有文件夹和各种文件。
目前遇到的问题是：
1. 单个文件的关键信息就是一个文件名，这个可以单独创建。 - 已经解决
2. 对于文件夹的情况相对复杂多了，需要有文件夹的名字；更需要在新创建的文件夹中填充文件或者
   其他子文件夹；子文件夹中继续嵌套有其他的文件夹和文件
3. 目前文件夹的数据组织使用字典来作为信息的处理数据结构，
4. 文件夹处理针对内容有三种场景：内容为空、单个文件、一个列表（列表中可能会嵌套有子字典数据）

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
root = {'root':[app, migrations, test, venv, 'requirements.txt', 'config.py', \
    'manage.py']}


# 下面都是零件方法，看看如何才能把这需求写的比较优雅
def mk_file(name):
    '''
    这个方法只用来创建空文件，只接受一个参数：文件的名字
    '''
    sys('touch %s' % name)


def mk_dir(name):
    '''
    这个方法只创建文件夹，只接受一个参数：文件夹的名字
    '''
    sys('mkdir %s' % name)
    
def feed_content(name, content):
    '''
    这个方法是为子文件夹中创建新的内容
    '''
    pass



