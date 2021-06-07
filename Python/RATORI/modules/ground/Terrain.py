import pygame as pg
from modules.ground.MapTest import map as _map_

class Terrain(object):

    _atlas_ = pg.image.load('images\\sprite.bmp')
    _atlas_.set_colorkey((255, 255, 255))
    _rate_ = 48

    def __init__(self):
        """ Окружение """
        self.map = _map_
        self.rate = self._rate_
        self.tile_atlas = {}
        self.tile_atlas = self.filling()
        self.start_point = 3050, 1896

    def filling(self):
        """ Зополняем Atlas таеломи """
        atlas = self._atlas_
        rate = self.rate
        size = (rate, rate)
        for row in range(atlas.get_height() // 48):
            for col in range(atlas.get_width() // 48):
                rect = (col * rate, row * rate)
                image = atlas.subsurface(rect, size)
                key = str(f'{row:0{2}}') + str(f'{col:0{2}}')
                self.tile_atlas[key] = image

        return self.tile_atlas


