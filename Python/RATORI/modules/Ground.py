from modules.Terrain import Terrain
import pygame as pg


class Ground(object):
    def __init__(self):
        """ Конструктор """
        self.terrain = Terrain()

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        self.terrain.draw(g)
