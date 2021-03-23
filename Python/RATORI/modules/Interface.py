import sys
from random import randint
import pygame as pg


class Interface(object):
    def __init__(self):
        """ Конструктор """
        pass

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        pg.draw.rect(g, '#047A00', (0, 500, 230, 220), 5)
