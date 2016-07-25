#!/usr/local/bin/python3
# _*_coding: utf-8


import os
import shutil


def move_over(src_dir, dest_dir):
    fileList = os.listdir(src_dir)
    for i in fileList:
        src = os.path.join(src_dir, i)
        dest = os.path.join(dest_dir, i)
        if os.path.exists(dest):
            if os.path.isdir(dest):
                move_over(src, dest)
                continue
            else:
                os.remove(dest)
        shutil.move(src, dest_dir)

src_dir = '/Users/john.leschinski/Desktop/testSrc'
dest_dir = '/Users/john.leschinski/Desktop/testMove'
move_over(src_dir, dest_dir)
