from modules.ground.Terrain import Terrain


class Ground(object):
    def __init__(self):
        """ Конструктор """
        self.terrain = Terrain()

    def update(self):
        """ Обнавление """
        pass

    def draw(self, g):
        """ Отрисовка """
        g.fill("darkgrey")
        for y in range(15):
            for x in range(27):
                key = self.terrain.map[y][x]
                tile = self.terrain.tile_atlas[key]
                g.blit(tile, (x * 48, y * 48))
