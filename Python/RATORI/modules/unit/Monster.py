import pygame as pg

class Monster(object):
    _atlas_ = pg.image.load('images\\Monster.png')
    _rate_ = 64

    def __init__(self):
        """Конструктор"""
        pg.init()
        self.rate = self._rate_
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.tile_atlas = []
        self.tile_atlas = self.filling()
        self.row = 0
        self.col = 0
        self.step = 0
        self.image = self.tile_atlas[self.row][self.col]
        self.speed = 0

    def update(self, turn):
        """Обновление"""
        if turn == 'stop':
            self.image = self.tile_atlas[self.row][self.col]
        else:
            if turn == 'right_down':
                self.col = 1
            elif turn == 'left_down':
                self.col = 7
            elif turn == 'left_up':
                self.col = 5
            elif turn == 'right_up':
                self.col = 3
            elif turn == 'right':
                self.col = 2
            elif turn == 'down':
                self.col = 0
            elif turn == 'left':
                self.col = 6
            elif turn == 'up':
                self.col = 4

            self.select()

    def draw(self, g):
        """Отрисовка"""
        self.image = self.tile_atlas[self.row][self.col]
        g.blit(self.image, self.rect)

    def select(self):
        self.speed += 1
        if self.speed >= 10:
            self.speed = 0
            self.row += 1
            if self.row >= 4:
                self.row = 0

    def filling(self):
        """Заполняем атлас тайлами"""
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // rate):
            self.tile_atlas.append([])
            for col in range(atlas.get_width() // rate):
                rect = (col * rate, row * rate)
                image = atlas.subsurface((rect, size))
                image = pg.transform.scale(image, (rate*2, rate*2))
                self.tile_atlas[row].append(image)
        return self.tile_atlas