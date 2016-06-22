#!/usr/local/bin/python3
# _*_coding: utf-8


import shutil
from os import listdir
from os.path import isfile, join
import subprocess


# 定义要处理文件的路径，此处为Mac的下载目录
download_path = '/Users/suntao/Downloads/'

# Home目录定义
root_path = '/Users/suntao/'

# 需要把对应的文件移动到目标路径，定义目标路径们
sketch_path = root_path + 'Documents/Sketch/'
docs_path = download_path + 'Docs/'
soft_path = download_path + 'Soft/'
pdf_path = root_path + 'Dropbox/Docs/'
image_path = root_path + 'Pictures/'


# 挑选出文件夹中所有是文件的信息，返回值赋值到一个list变量中
'''List all of the content in the Downloads folder and collect 
all of these file in a list'''
only_files = [f for f in listdir(download_path) if isfile(join(download_path, f))]


# Create the file lists base on extend file names
def files(ends_name):
	return [f for f in only_files if f.endswith(ends_name)]
	
sketch_file = files('.sketch')
word_file = files('.doc') + files('.docx')
excel_file = files('.xls') + files('.xlsx')
ppt_file = files('.ppt') + files('.pptx')
docs_file = word_file + ppt_file + excel_file + files('.txt') + files('.rtf')

soft_file = files('.dmg')
pdf_file = files('.pdf')
image_file = files('.jpg') + files('.jpeg') + files('.png') + files('.gif') + files('.bmp')

# 文件类型对应相关移动的目标文件夹
file_dict = {
	sketch_path: sketch_file,
	docs_path: docs_file,
	image_path: image_file,
	pdf_path: pdf_file,
	soft_path: soft_file
}

# Create a workflow for handling all of file types
def move_files(file_list, target_folder):
	for file in file_list:
		shutil.move(download_path + file, target_folder)
		
# Move all of files into their target folder for organization
for k, v in file_dict.items():
	move_files(v, k)
