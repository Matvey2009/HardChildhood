import pygame as pg
from modules.ground.Terrain import Terrain


class MiniMap(object):
    def __init__(self, size):
        """ Конструктор """
        self.size = size
        self.terrain = Terrain()
        self.count_x = len(self.terrain.map[0])
        self.count_y = len(self.terrain.map)
        self.rate = self.size[0] // (self.count_x * 3)
        self.rect = self.positon(self.size)
        self.hero = self.pos_hero(self.terrain.start_point)
        self.image = self.terrain.tile_atlas['0202']

    def update(self):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.rate = self.size[0] // (self.count_x * 3)
            self.rect = self.positon(self.size)
        self.hero = self.pos_hero(self.hero)

    def draw(self, g):
        """ Отрисовка """
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                tile = pg.transform.scale(tile, (self.rate, self.rate))
                g.blit(tile, (x*self.rate, y*self.rate + self.rect[1], self.rate, self.rate))

        pg.draw.circle(g, 'Blue', self.hero, 5)
        pg.draw.rect(g, 'Blue', self.rect, 5)

    def positon(self, size):
        """ Позиция """
        x1 = 1
        x2 = self.rate * self.count_x
        y2 = self.rate * self.count_y
        y1 = size[1] - y2
        print(size)
        return x1, y1, x2, y2

    def pos_hero(self, hero):
        """Расчёт позиции героя"""
        x = 193
        y = 623
        return x, y
