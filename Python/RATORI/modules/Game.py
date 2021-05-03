import pygame as pg
from modules.ground.Ground import Ground
from modules.Interface.Interface import Interface
from modules.unit.Hero import Hero


class Game(object):

    def __init__(self, size):
        """ Игра """
        self.size = size
        self.ground = Ground(size)
        self.interface = Interface(size)
        self.hero = Hero(size)
        self.hero.rect.center = self.positon(size)
        self.turn = 'stop'

    def update(self, e):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.hero.rect.center = self.positon(size)

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
        self.hero.update(self.turn)
        self.interface.update()

    def draw(self, g):
        """ Отрисовка """
        self.ground.draw(g)
        self.interface.draw(g)
        self.hero.draw(g)

    def positon(self, size):
        """ Позиция """
        pos_x = size[0] // 2
        pos_y = size[1] // 2
        return pos_x, pos_y