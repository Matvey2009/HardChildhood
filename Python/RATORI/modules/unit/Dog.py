import pygame as pg
from random import randint as r


class Dog(object):
    pg.init()
    _atlas_ = pg.image.load('images\\Dog.png')

    def __init__(self, size):
        """ Конструктор """
        self.row = 6
        self.col = 0
        self.step = 0
        self.speed = 3
        self.speedD = 2
        self.rate_x = 160
        self.rate_y = 130
        self.unit_turn = 8
        self.time_move = 60
        self.scroll_line = 10
        self.scroll = round(self.scroll_line / 1.4)
        self.title_atlas = []
        #self.title_atlas = self.filling()
        self.title_atlas = self._atlas_
        self.point_x = r(size[0] // 4, size[0] * 3 // 4)
        self.point_y = r(size[1] // 4, size[1] * 3 // 4)
        #self.image = self.title_atlas[self.row][self.col]
        self.image = self._atlas_
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """ Обнавление """
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 8)
            self.time_move = r(30, 150)
        self.time_move -= 1
        if self.unit_turn > 7:
            #self.image = self.title_atlas[6][0]
            self.image = self._atlas_
        else:
            self.col = self.unit_turn
            #self.image = self.select()


    def draw(self, g):
        """ Отрисовка """
        g.blit(self.image, self.rect)

    def select(self):
        """Выбор шага"""
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