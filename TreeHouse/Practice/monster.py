#! /usr/bin/python
# _*_coding: utf-8

import random
from combat import Combat

# 这种全局定义一种字典变量的方式不可用
# dict_item = {
#     'hit_points': 5,
#     'color': 'Blue',
#     'weapon': 'Roar',
#     'sound': 'Zing'
# }

COLORS = ['red', 'blue', 'gold', 'black', 'white', 'yellow', 'green']


# Works both on python2 and python 3
class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'Sword'
    sound = 'Roar'

    def __str__(self):
        return "{} {}, HP: {}, XP: {}".format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

    def __init__(self, **kwargs):
        # self.hit_points = dict_item.get('hit_points', 6)
        # self.color = dict_item.get('color', 'Gold')
        # self.weapon = dict_item.get('weapon', 'Sourd')
        # self.sound = dict_item.get('sound', 'Miao')
        self.hit_points = random.randint(self.min_hit_points,
                                         self.max_hit_points)
        self.experience = random.randint(self.min_experience,
                                         self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 2
    max_hit_points = 5
    min_experience = 3
    max_experience = 10
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 20
    min_experience = 6
    max_experience = 21
    sound = 'raaaaaaaaar'
