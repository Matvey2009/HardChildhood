import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):

    def __init__(self, size):
        """ Конструктор """
        self.size = size
        self.point_x = self.size[0] // 2
        self.point_y = self.size[1] // 2

    def update(self, turn):
        """ Обнавление """
        self.point_x, self.point_y = self.pos_unit(turn)
        self.point_x += 10
        self.point_y += 10

    def draw (self, g):
        """ Отрисовка """
        pg.draw.circle(g, (255, 69, 0), (self.point_x, self.point_y), 5)
