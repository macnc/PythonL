# #!/usr/local/bin/python
# # _*_coding: utf-8
#
#
# '''
# This file is for the practice script from function section of <Think Python 2E>
# '''
#
# Section practice I
def right_justify(s):
    space = 70 - len(s)
    for _ in range(70):
        print('|', end='')
    print()
    print(' '*space + s)


def do_twice(s):
    print_twice(s)
    print_twice(s)


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(f, args):
    for _ in range(4):
        f(args)


def print_spam():
    print('Spam is here')


# Section practice II
def print_plus():
    print('+', '- '*4, '+', '- '*4, '+')


def print_vertical():
    print('|', ' '*8, '|', ' '*8, '|')


def grade():
    for no in range(0, 11):
        if no in [0, 5, 10]:
            print_plus()
        else:
            print_vertical()



def real_grade():
    for i in range(9):
        if i % 2 == 0:
            print(' --' * 4 +' ')
        else:
            print('|  ' * 4 + '|')


if __name__ == '__main__':
    # do_twice('Spam')
    real_grade()
