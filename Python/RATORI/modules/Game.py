import pygame as pg
from modules.ground.Ground import Ground
from modules.unit.Hero import Hero
from modules.unit.Gangster import Gangster
from modules.unit.Monster import Monster
from modules.Interface.Interface import Interface


class Game(object):

    def __init__(self, size):
        """ Игра """
        self.size = size
        self.ground = Ground(self.size)
        self.interface = Interface(self.size)
        self.monster = Monster()
        self.gangster = Gangster()
        self.hero = Hero(self.size)
        self.hero.rect.center = self.positon(self.size)
        self.monster.rect.center = self.positon_monster(self.size)
        self.turn = 'stop'
        self.turn_m = 'stop'
        # self.random = 100-150
        # self.random = random
        # self.target

    def update(self, e):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.hero.rect.center = self.positon(size)
            self.hero.rect.center = self.positon_monster(size)


        # Смисок кликов клавиатуры
        keys = pg.key.get_pressed()

        if (keys[pg.K_RIGHT] and keys[pg.K_DOWN]):
            self.turn = 'right_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_DOWN]):
            self.turn = 'left_down'
        elif (keys[pg.K_LEFT] and keys[pg.K_UP]):
            self.turn = 'left_up'
        elif (keys[pg.K_RIGHT] and keys[pg.K_UP]):
            self.turn = 'right_up'
        elif (keys[pg.K_DOWN]):
            self.turn = 'down'
        elif (keys[pg.K_LEFT]):
            self.turn = 'left'
        elif (keys[pg.K_RIGHT]):
            self.turn = 'right'
        elif (keys[pg.K_UP]):
            self.turn = 'up'
        else:
            self.turn = 'stop'

        self.ground.update(self.size, self.turn)
        self.gangster.update(self.turn)
        self.monster.update(self.turn)
        self.hero.update(self.turn)
        hero = self.ground.point_x, self.ground.point_y
        gangster = self.ground.point_x, self.ground.point_y
        self.interface.update(hero)

    def draw(self, g):
        """ Отрисовка """
        self.ground.draw(g)
        self.gangster.draw(g)
        self.monster.draw(g)
        self.hero.draw(g)
        self.interface.draw(g)

    def positon(self, size):
        """ Позиция """
        pos_x = size[0] // 2
        pos_y = size[1] // 2

        return pos_x, pos_y

    def positon_monster(self, size):
        """ Позиция """
        pos_x = size[0] // 2 + 68
        pos_y = size[1] // 2

        return pos_x, pos_y


