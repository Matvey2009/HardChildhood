import pygame as pg
from modules.Ground import Ground
from modules.Unit import Unit
from modules.Interface import Interface


class Game(object):

    # GAME
    def __init__(self, size):
        self.size = size
        self.ground = Ground()
        self.unit = Unit()
        self.interface = Interface()
        self.unit.rect.center = self.positon(size)

    def update(self, e):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.unit.rect.center = self.positon(size)
        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 3
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 3
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x -= 3
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.unit.rect.x += 3

    def draw(self, g):
        """ Отрисовка """
        g.fill('grey')
        self.unit.draw(g)

    def positon(self, size):
        """ Позиция """
        pos_x = size[0] // 2
        pos_y = size[1] // 2
        return pos_x, pos_y