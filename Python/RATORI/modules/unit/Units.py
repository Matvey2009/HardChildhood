from modules.unit.Monster import Monster
from modules.unit.Gangster import Gangster
from modules.unit.Dog import Dog

class Units(object):
    def __init__(self, size):
        """ Конструктор """
        title_atlas = Gangster.filling()
        self.list_unit = []
        self.count = 1000
        for i in range(self.count):
            unit = Gangster(size, title_atlas)
            self.list_unit.append(unit)

        for i in range(self.count - 40):
            unit = Dog(size)
            self.list_unit.append(unit)

        self.monster = Monster()
        self.speed = 3
        self.speedD = 2

    def update(self, turn):
        """ Обнавление """
        for unit in self.list_unit:
            unit.rect.x, unit.rect.y = self.move_unit(unit)
            unit.update(turn)
        self.monster.update(turn)

    def draw(self, g):
        """ Отрисовка """
        for unit in self.list_unit:
            unit.draw(g)
        self.monster.draw(g)

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