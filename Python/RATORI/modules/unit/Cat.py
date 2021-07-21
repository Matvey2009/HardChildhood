import pygame as pg
from random import randint as r
from modules.unit.Abstract import Abstract


class Cat(Abstract):

    # Отрисовка Трраина
    @staticmethod
    def filling():
        """Заполняем атлас тайлами"""
        pg.init()
        rate = 32 * 2
        atlas = pg.image.load('images\\cat.png')
        atlas = pg.transform.scale(atlas, (9 * rate, 4 * rate))
        tile_atlas = []
        for row in range(atlas.get_height() // rate):
            tile_atlas.append([])
            for col in range(atlas.get_width() // rate):
                rect = (rate * col, rate * row)
                image = atlas.subsurface((rect, (rate, rate)))
                tile_atlas[row].append(image)
        return tile_atlas

    def __init__(self, size, tile_atlas):
        """Конструктор"""
        self.rate_x = 32 * 2
        self.rate_y = 32 * 2
        self.step = 0
        self.row = 0
        self.col = 8
        self.time_move = 20
        self.scroll_line = 10
        self.unit_turn = 8
        self.scroll = self.scroll_line / 1.4
        self.tile_atlas = tile_atlas
        self.point_x = r(size[0] // 8, size[0] * 3 // 4)
        self.point_y = r(size[1] // 8, size[1] * 3 // 4)
        self.image = self.tile_atlas[self.row][self.col]
        self.rect = pg.Rect(self.point_x, self.point_y, self.rate_x, self.rate_y)

    def update(self, turn):
        """Обновление"""
        self.rect.x, self.rect.y = self.pos_unit(turn)
        if self.time_move < 1:
            self.unit_turn = r(0, 8)
            self.time_move = r(30, 150)
        self.time_move -= 1
        if self.unit_turn > 7:
            self.image = self.tile_atlas[0][8]
        else:
            self.col = self.unit_turn
            self.image = self.select()

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.image, self.rect)

    def select(self):
        """Выбор картинки шага"""
        if self.step > 10:
            if self.row >= 3:
                self.row = 0
            else:
                self.row += 1
                self.step = 0
        else:
            self.step += 5
        return self.tile_atlas[self.row][self.col]
