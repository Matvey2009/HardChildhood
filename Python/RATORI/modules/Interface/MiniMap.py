import pygame as pg
from modules.ground.Terrain import Terrain


class MiniMap(object):
    def __init__(self, size):
        """ Конструктор """
        self.ricex = 482
        self.size = size
        self.terrain = Terrain()
        self.count_x = len(self.terrain.map[0])
        self.count_y = len(self.terrain.map)
        self.rate = 6
        self.rect = self.positon(self.size)
        self.image = self.terrain.tile_atlas['0202']

    def update(self):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.rect = self.positon(self.size)

    def draw(self, g):
        """ Отрисовка """
        for y in range(self.count_y):
            for x in range(self.count_x):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                g.blit(tile, (x*self.rate, y*self.rate+self.ricex, self.rate, self.rate))

        pg.draw.rect(g, 'Blue', (self.rect, (self.size[0] // 3, self.size[1] // 3)), 5)

    def positon(self, size):
        """ Позиция """
        pos_x = 0
        pos_y = size[1] // 3 * 2
        return pos_x, pos_y