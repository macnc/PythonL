#!/usr/local/bin/python
# _*_coding: utf-8

# 写好的函数没有用到极致,该需要重新调用的没有做调用
# 此代码作为教训,返回观看时做修改


from turtle import *
from math import *


# 更加泛化的多边形打印函数
def polyline(t, n, length, angle):
    for _ in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle= 360/n
    polyline(t, n, length, angle)


# 圆形泛华打印函数,加入打印圆形的完整性
def arc(t, r, angle):
    '''
    打印一部分圆形的函数,通过传递三个参数来完成函数的调用
    函数最终返回的结果会是通过Turtle对象打印出一个指定角度的圆弧
    :param t: 类型是Turtle对象, 预先定义好的Turtle对象变量
    :param r: 参数类型是float浮点数类型, 圆弧的半径长度
    :param angle: 参数类型是float浮点数类型, 要打印成型圆弧的角度
    :return: None, 无具体的返回值
    '''
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


# 正方形打印函数
def square(t, length):
    polygon(t, 4, length)

# 圆形打印函数
def circle(t, r):
    arc(t, r, 360)


def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(angle)
    arc(t, r, angle)

bob = Turtle()
if __name__ == '__main__':
    for _ in range(7):
        petal(bob, 88, 90)