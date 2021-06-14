import pygame as pg
from random import randint as r


class Gangster(object):
    pg.init()
    _atlas_ = pg.image.load('images\\gangster.png')

    def __init__(self):
        """ Конструктор """
        self.row = 6
        self.col = 0
        self.step = 0
        self.rate_x = 160
        self.rate_y = 130
        self.scroll_line = 10
        self.scroll = round(self.scroll_line / 1.4)
        self.title_atlas = []
        self.title_atlas = self.filling()
        self.point_x, self.point_y = (r(400, 600), r(200, 400))
        self.image = self.title_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """ Обнавление """
        self.rect.x, self.rect.y = self.pos_unit(turn)

    def draw(self, g):
        """ Отрисовка """
        g.blit(self.image, self.rect)

    def select(self):
        if self.step > 120:
            if self.row > 4:
                self.row = 0
            else:
                self.row += 1
                self.step = 0
        else:
            self.step += 12

        return self.title_atlas[self.row][self.col]

    def filling(self):
        """ Зополняем Atlas таеломи """
        atlas = self._atlas_
        size = (self.rate_x, self.rate_y)
        for row in range(atlas.get_height() // self.rate_y):
            self.title_atlas.append([])
            for col in range(atlas.get_width() // self.rate_x):
                rect = (col * self.rate_x, row * self.rate_y)
                image = atlas.subsurface(rect, size)
                self.title_atlas[row].append(image)

        return self.title_atlas

    def pos_unit(self, turn):
        """Позиция unit"""
        if turn == "right_down":
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_down':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_up':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif turn == 'right_up':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line

        return self.point_x, self.point_y