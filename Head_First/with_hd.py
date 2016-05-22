#! /usr/local/bin/python3
# _*_coding: utf-8

import os

man = []
other = []
'''
用with语句，可以解决这些问题：
1、不用再加入Finally模块来做必须要做的一些操作，with会帮你处理
2、文件打开之后，不用再手动close简化语句，把精力放到真正核心的部分
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
            except ValueError:
                pass

    # 有了with，不用再加入关闭文件流操作了，因为with会自动处理这些东西
    # data.close()
except IOError:
    print('The datafile is missing!')

try:

    # 方案一或者叫方式一；当然还有另外一种写法，简化代码
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt', 'w') as other_file:
        print(other, file=other_file)

    # 方案二，将with要处理的语句写到一行代码里，这样可以简化输入
    with open('man_txt.txt', 'w') as man_data, open('other_txt.txt', 'w') \
    as other_data:
        print(man, file=man_data)
        print(other, file=other_data)

except IOError as err:
    print('File Error!' + str(err))

# 不论什么情况下，这个模块下的代码都会执行，确保文件不会因为程序的bug造成损坏
# 有了with，不用再加入finally模块了
# finally:
#     if man_file in locals():
#         man_file.close()
#     if other_file in locals():
#         other_file.close()
