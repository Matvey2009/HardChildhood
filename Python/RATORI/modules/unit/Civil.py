import pygame as pg
from random import randint as r
from modules.unit.Abstract import Abstract


class Civil(Abstract):
    pg.init()

    @staticmethod
    def filling():
        """Заполняет атлас"""
        _atlas_ = pg.image.load("images\Сivil.png")
        _rate_ = 35
        size = (_rate_, _rate_)
        tile_atlas = []
        for row in range(8):
            tile_atlas.append([])
            for col in range(9):
                rect = (col * _rate_, row * _rate_)
                image = _atlas_.subsurface(rect, size)
                image = pg.transform.scale(image, (72, 72))
                tile_atlas[row].append(image)
        return tile_atlas

    def __init__(self, size, tile_atlas):
        """Конструктор"""
        self.rate = 35
        self.size = size
        self.tile_atlas = tile_atlas
        self.row = 0
        self.col = 0
        self.step = 0
        self.step = 0
        self.unit_turn = 8
        self.image = self.tile_atlas[self.row][self.col]
        self.point_x, self.point_y = (r(self.size[0] // 4, self.size[0] // 4 * 3)), (
            r(self.size[1] // 4, self.size[1] // 4 * 3))
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate, self.rate)
        self.time_move = 60
        self.speed = 1

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 10)
            self.time_move = r(80, 160)
        self.time_move -= 1
        if self.unit_turn > 7:
            self.image = self.tile_atlas[0][0]
        else:
            self.row = self.unit_turn
            self.image = self.select()

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)

    def pos_unit(self, turn):
        """Позиция юнита"""
        if turn == 'right_down':
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
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line

        return self.point_x, self.point_y

    def select(self):
        """Заполнение"""
        if self.step > 8:
            if self.col > 7:
                self.col = 0
            else:
                self.col += 1
                self.step = 0
        else:
            self.step += self.speed
        return self.tile_atlas[self.row][self.col]