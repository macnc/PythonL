#! /usr/local/bin/python3
# _*_coding: utf-8

import os

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file)
    print(other, file=other_data)

except IOError as err:
    print('File Error!' + str(err))

# 不论什么情况下，这个模块下的代码都会执行，确保文件不会因为程序的bug造成损坏
finally:
    if man_file in locals():
        man_file.close()
    if other_file in locals():
        other_file.close()
