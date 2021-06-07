import pygame as pg

class Bullet(object):
    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.bullet = 24
        self.font = pg.font.Font(None, 36)
        self.text = self.font.render(str(self.bullet), True, 'Black')

    def update(self, size):
        """Обновление"""
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.text, (self.size[0]-50, self.size[1]-50))