from modules.Interface.MiniMap import MiniMap
from modules.Interface.Score import Score

class Interface(object):
    def __init__(self, size):
        """ Конструктор """
        self.size = size
        self.minimap = MiniMap(self.size)
        self.score.update()

    def update(self, hero):
        """ Обнавление """
        self.minimap.update(hero)

    def draw(self, g):
        """ Отрисовка """
        self.minimap.draw(g)
        self.score.draw(g)
