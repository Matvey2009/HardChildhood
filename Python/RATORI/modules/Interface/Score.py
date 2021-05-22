import pygame as pg


class Score(object):
    """ Очки игры """

    def __init__(self):
        """ Очки """
        score = 0
        self.score = score
        self.font = pg.font.Font(None, 36)

    def update(self):
        """ Обновление """
        pass

    def draw(self, g):
        """ Отрисовка """
        text = self.font.render(str(self.score), True, 180, 0, 0)
        g.blit(text, 100, 100)

