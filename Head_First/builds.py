#! /usr/local/bin/python3
# _*_coding: utf-8

import os

class Folder(list):
	# Create the basic information for the structure of the folder
	def __init__(self, name, c_list=[], f_name=None):
		'''The constrcutor method for creating new Folder object.
		We will add the basic information data here.'''
		self.name = name
		self.content = c_list
		self.father = f_name

		# After the basic data has been created, we will invoke the
		# other method for create reall stuff in the current folder
		# object.
		for item in self.content:
			if isinstance(item, Folder):
				# Invoke the Folder object information for 
				# creating sub-folder with contents
				mk_dir(item.name)
			else:
				mk_file(item)

	# Public method for adding content in the folder
	def add_content(self, s_list):
		'''This is a public method for adding new content in the
		current folder object.'''
		try:
			self.content = self.content.extend(s_list)
		except ValueError as e:
			print('List value error: ' + str(e))

		# After fill the data information in the folder content list,
		# we will invoke the mk_dir and mk_file method for make real
		# content.


	# Create file in the folder
	def mk_file(self, name, path=None):
		'''Get the file information from the content list.
		If the data type is string, then create the file with
		invoking the os.system('') methon with shell.'''
		if path is not None:
			os.system('touch %s/%s' % (path, name))
		else:
			os.system('touch %s' % name)


	def mk_dir(self, name, path=None):
		'''Get the folder information from the content list.
		If the data type in content list is list type, then 
		invoke the Folder class constructor function for making
		new folder object with some content.'''
		if path is not None:
			os.system('mkdir %s/%s' % name)
