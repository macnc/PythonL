#! /usr/bin/python
# _*_coding: utf-8

dict_item = {
    'hit_points': 5,
    'color': 'Blue',
    'weapon': 'Roar',
    'sound': 'Zing'
}


class Monster:
    def __init__(self, **dict_item):
        self.hit_points = dict_item.get('hit_points', 6)
        self.color = dict_item.get('color', 'Gold')
        self.weapon = dict_item.get('weapon', 'Sourd')
        self.sound = dict_item.get('sound', 'Miao')

    def battlecry(self):
        return self.sound.upper()


mini = Monster()
