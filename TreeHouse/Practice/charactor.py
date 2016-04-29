#! /usr/bin/python
# _*_coding: utf-8

import random
from combat import Combat


class Charactor(Combat):
    attact_limit = 10
    experience = 0
    hit_points = 10

    # overwrite the method inheritance
    def attact(self):
        roll = random.randint(1, self.attact_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 'a':
                return 'axe'
            elif weapon_choice == 's':
                return 'sword'
            else:
                return 'bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()

        for key, value in kwargs.items():
            setattr(self, key, value)
