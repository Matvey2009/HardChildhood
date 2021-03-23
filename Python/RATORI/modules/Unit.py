import pygame as pg

class Unit(object):
    pg.init()
    sound = pg.mixer.Sound('sounds\\S.mp3')
    _image_ = pg.image.load('images\\bag.png')

    # Unit
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    # Отрисовка
    def draw(self, g):
        g.blit(self.image, self.rect)
        if self.rect.x == 100:
            pg.mixer.Sound.play(self.sound)
