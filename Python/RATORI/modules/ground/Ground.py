from modules.ground.Terrain import Terrain
import pygame as pg


class Ground(object):
    def __init__(self, size):
        """ Конструктор """
        self.size = size
        self.terrain = Terrain()
        self.surface = pg.Surface(size)
        self.rect = self.surface.get_rect()
        self.point_x, self.point_y = self.terrain.start_point
        self.max_x = len(self.terrain.map[0]) * self.terrain.rate
        self.max_y = len(self.terrain.map) * self.terrain.rate
        # Шрифт для кода
        pg.font.init()
        self.font = pg.font.SysFont("arial", 12, True)

    def update(self, size, turn):
        """ Обнавление """
        scrole_line = 10
        scrole = round(scrole_line / 1.4)

        if turn == "right_down":
            self.point_x += scrole
            self.point_y += scrole
        elif turn == 'left_down':
            self.point_x -= scrole
            self.point_y += scrole
        elif turn == 'left_up':
            self.point_x -= scrole
            self.point_y -= scrole
        elif turn == 'right_up':
            self.point_x += scrole
            self.point_y -= scrole
        elif turn == 'down':
            self.point_y += scrole_line
        elif turn == 'left':
            self.point_x -= scrole_line
        elif turn == 'right':
            self.point_x += scrole_line
        elif turn == 'up':
            self.point_y -= scrole_line

        # Края краты
        if self.point_x < self.size[0] // 2 + scrole:
            self.point_x = self.size[0] // 2 + scrole
        if self.point_x >= self.max_x - size[0] // 2 - self.terrain.rate:
            self.point_x = self.max_x - size[0] // 2 - self.terrain.rate

        if self.point_y < self.size[1] // 2 + scrole:
            self.point_y = self.size[1] // 2 + scrole
        if self.point_y >= self.max_y - size[1] // 2 - self.terrain.rate:
            self.point_y = self.max_y - size[1] // 2 - self.terrain.rate

        if self.point_y < 1:
            self.point_y = 1

        self.select()

    def draw(self, g):
        """ Отрисовка """
        g.fill("darkgrey")
        g.blit(self.surface, self.rect)

    def select(self):
        """ Отрисовка поверхности """
        rate = self.terrain.rate
        # Граница окна
        x_left = self.point_x - self.size[0] // 2
        x_right = x_left + self.size[0]
        y_top = self.point_y - self.size[1] // 2
        y_button = y_top + self.size[1]
        for y in range(y_top // rate, y_button // rate+1):
            for x in range(x_left // rate, x_right // rate+1):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                self.surface.blit(tile, (x * rate - x_left, y * rate - y_top, rate , rate))

                # Коды таелов
                # text = self.font.render((str(y) + "-" + str(x)), True, "Blue")
                # text_rect = text.get_rect()
                # self.surface.blit(text, (x * rate - x_left + 4, y * rate - y_top + 16), text_rect)
