import pygame as pg


class Score(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.point = 0
        self.speed = 0
        self.font = pg.font.Font(None, 36)

    def update(self, size):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
        self.speed += 1
        if self.speed > 10:
            self.point += 1
            self.speed = 0

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.font.render(str(self.point), True, 'White'), (self.size[0]-50, 0))
