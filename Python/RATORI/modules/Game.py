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
        self.positon()

    def update(self, e):
        """ Обнавление """
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

    def positon(self):
        """ Позиция """
        self.unit.rect.x = self.size[0] // 2 - self.unit.rect.width // 2
        self.unit.rect.y = self.size[1] // 2 - self.unit.rect.height // 2