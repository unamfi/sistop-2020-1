#!/usr/bin/python3
# -*- coding: utf-8 -*-

from string import ascii_uppercase
from random import choice, randint

class Proceso:

    def __init__(self, tick_lim: list, llegada_lim: list):
        self.color_names = ['\033[31m','\033[32m','\033[33m','\033[34m',
                            '\033[36m','\033[37m','\033[91m','\033[92m',
                            '\033[93m','\033[94m','\033[95m']
        self.color = self.color_names[randint(0,len(self.color_names)-1)]
        self.nombre = self.color + "[" + str(choice(ascii_uppercase)) + "]\033[0m"
        self.t = randint(tick_lim[0], tick_lim[1])
        self.llegada = randint(llegada_lim[0], llegada_lim[1])
