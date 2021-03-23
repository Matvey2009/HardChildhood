import pygame as pg

class Terrain(object):

    _atlas_ = pg.image.load('images\\sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))

    def __init__(self):
        self.atlas = self._atlas_
        self.rect = self.atlas.get_rect()

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        g.blit(self.atlas, self.rect)
