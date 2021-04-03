import pygame as pg


class Hero(object):

    _atlas_ = pg.image.load('images\\Hero.png')
    _rate_ = 64

    def __init__(self, size):
        """ Конструктор """
        self.rate = self._rate_
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.rect = pg.Rect(0, 0, self.rate, self.rate)

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        image = self.tile_atlas[4][7]
        g.blit(image, self.rect)

    def filling(self):
        """ Зополняем Atlas таеломи """
        atlas = self._atlas_
        size = (self.rate, self.rate)
        for row in range(atlas.get_height() // self.rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // self.rate):
                rect = (col * self.rate, row * self.rate)
                image = atlas.subsurface(rect, size)
                image = pg.transform.scale(image, (self.rate * 2, self.rate * 2))
                self.tile_atlas[row].append(image)

        return self.tile_atlas