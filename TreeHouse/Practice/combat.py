#! /usr/bin/python
# _*_coding: utf-8

import random


class Combat:
    dodge_limit = 6
    attact_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def attact(self):
        roll = random.randint(1, self.attact_limit)
        return roll > 4
