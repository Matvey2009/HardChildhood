import pygame as pg


class MiniMap(object):
    def __init__(self, size):
        """ Конструктор """
        self.size = size
        self.rect = self.positon(self.size)

    def update(self):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            self.rect = self.positon(self.size)

    def draw(self, g):
        """ Отрисовка """
        pg.draw.rect(g, '#047A00', (self.rect, (self.size[0] // 3, self.size[1] // 3)), 5)

    def positon(self, size):
        """ Позиция """
        pos_x = 0
        pos_y = size[1] // 3 * 2
        return pos_x, pos_y