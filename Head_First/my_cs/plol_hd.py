#! /usr/local/bin/python3
# _*_coding: utf-8

try:
    from nester import print_lol
except ImportError as e:
    print('The error: ' + str(e))


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
                # print("The error detail: <" + str(er) + '>')
                pass
            

    # 有了with，不用再加入关闭文件流操作了，因为with会自动处理这些东西
    # data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.txt', 'w') as man_data, open('other_data.txt', 'w') \
        as other_data:
        print_lol(man, fn=man_data)
        print_lol(other, fn=other_data)

except IOError as err:
    print('File Error: <' + str(err) + '>')
