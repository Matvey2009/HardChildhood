import pygame as pg
from random import randint as r
from modules.unit.Abstract import Abstract

class Dog(Abstract):

    @staticmethod
    def filling():
        """ Зополняем Atlas таеломи """
        pg.init()
        rate_x = 48
        rate_y = 48
        atlas = pg.image.load('images\\doge .png')
        atlas = pg.transform.scale(atlas, (5 * rate_x, 2 * rate_y))
        title_atlas = []
        for row in range(atlas.get_height() // rate_y):
            title_atlas.append([])
            for col in range(atlas.get_width() // rate_x):
                rect = (col * rate_x, row * rate_y)
                image = atlas.subsurface(rect, (rate_x, rate_y))
                title_atlas[row].append(image)
        return title_atlas

    def __init__(self, size, title_atlas):
        """ Конструктор """
        self.row = 0
        self.col = 0
        self.step = 0
        self.speed = 3
        self.speedD = 2
        self.rate_x = 48
        self.rate_y = 48
        self.unit_turn = 8
        self.time_move = 60
        self.scroll_line = 10
        self.scroll = round(self.scroll_line / 1.4)
        self.title_atlas = title_atlas
        self.point_x = r(size[0] // 4, size[0] * 3 // 4)
        self.point_y = r(size[1] // 4, size[1] * 3 // 4)
        self.image = self.title_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """ Обнавление """
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 8)
            self.time_move = r(20, 100)
        self.time_move -= 1
        if self.unit_turn == 0:
            self.image = self.title_atlas[0][0]
        else:
            self.row = 1
            self.image = self.select()


    def draw_unit(self, g):
        """ Отрисовка """
        g.blit(self.image, self.rect)

    def select(self):
        """Выбор шага"""
        self.col += 1
        if self.col > 4:
            self.col = 0
        return self.title_atlas[self.row][self.col]
