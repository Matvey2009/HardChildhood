from modules.unit.Gangster import Gangster
from modules.unit.Civil import Civil
from modules.unit.Cat import Cat
from modules.unit.Adapter import Adapter
from modules.unit.Shot import Shot


class Units(object):

    def __init__(self, size):
        """ Конструктор """
        title_atlas = Gangster.filling()
        civil_atlas = Civil.filling()
        cat_atlas = Cat.filling()
        self.size = size
        self.list_unit = []
        self.list_shot = []
        self.shot = Shot()
        self.list_shot.append(self.shot)
        self.count = 50
        for i in range(self.count):
            unit = Gangster(size, title_atlas)
            self.list_unit.append(unit)
        title_atlas = Adapter.filling()
        for i in range(self.count - 40):
            unit = Adapter(size, title_atlas)
            self.list_unit.append(unit)
        for i in range(self.count - 30):
            unit = Civil(size, civil_atlas)
            self.list_unit.append(unit)
        for i in range(self.count - 30):
            unit = Cat(size, cat_atlas)
            self.list_unit.append(unit)
        self.speed = 3
        self.speedD = 2

    def update(self, turn):
        """ Обнавление """
        for unit in self.list_unit:
            unit.rect.x, unit.rect.y = self.move_unit(unit)
            if unit.rect.collidepoint(self.size[0] // 2, self.size[1] // 2):
                unit.arrest = True
                unit.unit_turn = 8
            unit.update(turn)
        for self.shot in self.list_shot:
            self.shot.update()

    def draw(self, g):
        """ Отрисовка """
        for unit in self.list_unit:
            unit.draw(g)
        for self.shot in self.list_shot:
            self.shot.draw(g)


    def move_unit(self, unit):
        """Движение юнита"""
        if unit.unit_turn == 1:
            unit.point_x += self.speedD
            unit.point_y += self.speedD
        elif unit.unit_turn == 7:
            unit.point_x -= self.speedD
            unit.point_y += self.speedD
        elif unit.unit_turn == 5:
            unit.point_x -= self.speedD
            unit.point_y -= self.speedD
        elif unit.unit_turn == 3:
            unit.point_x += self.speedD
            unit.point_y -= self.speedD
        elif unit.unit_turn == 2:
            unit.point_x += self.speed
        elif unit.unit_turn == 0:
            unit.point_y += self.speed
        elif unit.unit_turn == 6:
            unit.point_x -= self.speed
        elif unit.unit_turn == 4:
            unit.point_y -= self.speed

        return unit.point_x, unit.point_y