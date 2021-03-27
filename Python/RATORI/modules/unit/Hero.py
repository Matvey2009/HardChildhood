import pygame as pg


class Hero(object):

    _atlas_ = pg.image.load('images\\Hero.jpg')
    _atlas_.set_colorkey((255, 255, 255))

    def __init__(self, size):
        """ Конструктор """
        self.rate = 92
        self.rect = pg.Rect(0, 0, self.rate, self.rate)

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        rate = self.rate
        size = (rate, rate)
        rect = self.rect
        image = self._atlas_.subsurface((0 ,0), size)
        g.blit(image, self.rect)