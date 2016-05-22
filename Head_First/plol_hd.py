#! /usr/local/bin/python3
# _*_coding: utf-8


from print_lol import *
# # try:
# #     from nester import *
# # except ImportError as e:
# #     print("There's no packages like name nester on local: <" + str(e) + '>')
# import sys


man = []
other = []
'''
本文件中使用之前章节建立的print_lol方法来目前的信息保存到txt文件中
'''
try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError as er:
                print("The detail: <" + str(er) + '>')

    # 有了with，不用再加入关闭文件流操作了，因为with会自动处理这些东西
    # data.close()
except IOError:
    print('The datafile is missing!')

try:
    # 方案一或者叫方式一；当然还有另外一种写法，简化代码
    with open('man_data.txt', 'w') as man_file:
        print_lol(man, fn=man_file)
    with open('other_data.txt', 'w') as other_file:
        print_lol(other, fn=other_file)

    # 方案二，将with要处理的语句写到一行代码里，这样可以简化输入
    # with open('man_txt.txt', 'w') as man_data, open('other_txt.txt', 'w') \
    #     as other_data:
    #     print_lol(man, fn=man_data)
    #     print_lol(other, fn=other_data)

except IOError as err:
    print('File Error: <' + str(err) + '>')
