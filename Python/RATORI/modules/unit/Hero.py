import pygame as pg


class Hero(object):

    _atlas_ = pg.image.load('images\\Hero.png')
    _rate_ = 64

    def __init__(self, size):
        """ Конструктор """
        self.rate = self._rate_
        self.title_atlas = []
        self.title_atlas = self.filling()
        self.rect = pg.Rect(0, 0, self.rate, self.rate)
        self.speed = 0
        self.row = 0
        self.col = 0
        self.step = 0
        self.image = self.title_atlas[self.row][self.col]


    def update(self, turn):
        """ Обнавление """
        if turn == 'stop':
            self.image = self.title_atlas[0][0]
        else:
            if turn == 'right_down':
                self.col = 1
            elif turn == 'left_down':
                self.col = 7
            elif turn == 'left_up':
                self.col = 5
            elif turn == 'right_up':
                self.col = 3
            elif turn == 'down':
                self.col = 0
            elif turn == 'left':
                self.col = 6
            elif turn == 'up':
                self.col = 4
            elif turn == 'right':
                self.col = 2

        self.select()


    def draw(self, g):
        """ Отрисовка """
        self.image = self.title_atlas[self.row][self.col]
        g.blit(self.image, self.rect)

    def select(self):
        self.speed += 1
        if self.speed >= 10:
            self.row += 1
            self.speed = 0
            if self.row >= 4:
                self.row = 1

    def filling(self):
        """ Зополняем Atlas таеломи """
        atlas = self._atlas_
        size = (self.rate, self.rate)
        for row in range(atlas.get_height() // self.rate):
            self.title_atlas.append([])
            for col in range(atlas.get_width() // self.rate):
                rect = (col * self.rate, row * self.rate)
                image = atlas.subsurface(rect, size)
                image = pg.transform.scale(image, (self.rate * 2, self.rate * 2))
                self.title_atlas[row].append(image)

        return self.title_atlas