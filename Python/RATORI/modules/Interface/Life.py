import pygame as pg


class Life(object):
    """ Уровень жизни """

    def __init__(self):
        """ Жизнь """
        self.life = 100
        self.font = pg.font.Font(None, 36)

    def update(self):
        """ Обновление """
        pass

    def draw(self, g):
        """ Отрисовка """
        text = self.font.render(str(self.life), True, 'Green')
        g.blit(text, (0, 0))