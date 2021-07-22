import pygame as pg
from modules.unit.Abstract import Abstract


class Shot(Abstract):

    def __init__(self, size, turn):
        """ Конструктор """
        self.speed = 0
        self.size = size
        self.shot_turn = turn
        self.point_x = self.size[0] // 2
        self.point_y = self.size[1] // 2

    def update(self, turn):
        """ Обнавление """
        self.point_x, self.point_y = self.pos_unit(turn)
        self.pos_shot()

    def draw (self, g):
        """ Отрисовка """
        pg.draw.circle(g, (255, 69, 0), (self.point_x, self.point_y), 5)

    def pos_shot(self):
        self.scroll_line = 20
        self.scroll = round(self.scroll_line / 1.4)
        if self.shot_turn == 'right_down':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif self.shot_turn == 'left_down':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif self.shot_turn == 'left_up':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif self.shot_turn == 'right_up':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif self.shot_turn == 'right' or self.shot_turn == 'stop':
            self.point_x += self.scroll_line
        elif self.shot_turn == 'down':
            self.point_y += self.scroll_line
        elif self.shot_turn == 'left':
            self.point_x -= self.scroll_line
        elif self.shot_turn == 'up':
            self.point_y -= self.scroll_line
        return self.point_x, self.point_y
