import pygame as pg

class Unit(object):
    pg.init()
    sound = pg.mixer.Sound('sounds\\S.mp3')
    _image_ = pg.image.load('images\\bag.png')

    def __init__(self):
        """ Unit """
        self.image = self._image_
        self.rect = self.image.get_rect()

    def draw(self, g):
        """ Отрисовка """
        g.blit(self.image, self.rect)
        if self.rect.x == 100:
            pg.mixer.Sound.play(self.sound)
