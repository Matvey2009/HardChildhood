import pygame as pg


class Shot(object):

    def __init__(self):
        """ Конструктор """
        self.x = 100
        self.y = 100
        self.point = (self.x, self.y)

    def update(self):
        """ Обнавление """
        self.x += 1
        self.y += 1
        self.point = (self.x, self.y)

    def draw (self, g):
        """ Отрисовка """
        pg.draw.circle(g, (255, 69, 0), self.point, 5)
