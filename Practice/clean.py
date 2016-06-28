#!/usr/local/bin/python3
# _*_coding: utf-8

# Author: SunTao
# Last updated: Monday, June 27, 2016 at 11:28:11 AM

import shutil
from os import listdir, remove
from os.path import isfile, join, exists
import subprocess


# My home folder
root_path = '/Users/suntao/'

# Global variable for defination of the downloads folder on Mac
download_path = '/Users/suntao/Downloads/'


# The target folder where the specific file moved to
sketch_path = root_path + 'Documents/Sketch/'
docs_path = download_path + 'Docs/'
soft_path = download_path + 'Soft/'
dev_path = download_path + 'Dev/'
pdf_path = root_path + 'Dropbox/Docs/'
image_path = root_path + 'Pictures/'
ms_path = download_path + 'Mindset/'


# The current file list in downloads folder.
'''List all of the content in the Downloads folder and collect
all of these file in a list'''
only_files = [f for f in listdir(download_path) if isfile(join(download_path, f))]


# The function for creating the file lists base on the extended file names.
def files(ends_name):
	return [f for f in only_files if f.endswith(ends_name)]

# Create the file lists base on the specific file extended file names.
# The segment of the code below is defination of the for the work documents.
sketch_file = files('.sketch')
word_file = files('.doc') + files('.docx')
excel_file = files('.xls') + files('.xlsx')
ppt_file = files('.ppt') + files('.pptx')
docs_file = word_file + ppt_file + excel_file + files('.txt') + files('.rtf')

# This part of the code is defination of the  for the specific using
# as personal.
soft_file = files('.dmg')
mindset_file = files('.xmind')
pdf_file = files('.pdf')
dev_file = files('.log') + files('.dat')
image_file = files('.jpg') + files('.jpeg') + files('.png') + files('.gif') + files('.bmp')

# Key: destiny path for moving.
# Value: The list of specific file types.
file_dict = {
	sketch_path: sketch_file,
	docs_path: docs_file,
	image_path: image_file,
	pdf_path: pdf_file,
	soft_path: soft_file,
	dev_path: dev_file,
	ms_path: mindset_file
}

# Create a workflow for handling all of file types
def move_files(file_list, dest_dir):
	'''
	1. 如果目标目录中含有待移动的文件，删除目标
	2. 参数分别为：需要移动的文件列表为第一个参数，要移动到的目录为第二个参数
	3. 该函数中使用了全局变量下载目录的字符串变量：download_path
	4. 此方法中调用的join(), remove(), exists()方法均引用于os package
	'''
	for file in file_list:
		src = join(download_path, file)
		dest = join(dest_dir,file)
		if exists(dest):
			remove(dest)
		else:
			shutil.move(src, dest_dir)

# Move all of files into their target folder for organization
# 字典变量的key值(k)为特定文件类型需要移动到的目录位置字符串，file_list列表unhashable.
# 所以字典变量的Value值(v)为特定文件类型的文件名列表，key值只能为字符串的path地址。
for k, v in file_dict.items():
	move_files(v, k)
