import pygame as pg
from random import randint as r


class Gangster(object):

    @staticmethod
    def filling():
        """ Зополняем Atlas таеломи """
        pg.init()
        rate_x = 80
        rate_y = 65
        atlas = pg.image.load('images\\gangster.png')
        atlas = pg.transform.scale(atlas, (8 * rate_x, 9 * rate_y))
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
        self.row = 6
        self.col = 0
        self.step = 0
        self.speed = 3
        self.speedD = 2
        self.rate_x = 80
        self.rate_y = 65
        self.arrest = False
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
        if not self.arrest:
            if self.time_move < 1:
                self.unit_turn = r(0, 8)
                self.time_move = r(30, 150)
            self.time_move -= 1
            if self.unit_turn > 7:
                self.image = self.title_atlas[6][0]
            else:
                self.col = self.unit_turn
                self.image = self.select()
        else:
            self.image = self.title_atlas[8][self.col]


    def draw(self, g):
        """ Отрисовка """
        g.blit(self.image, self.rect)
        pg.draw.rect(g, 'black', self.rect, 1)  ########

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