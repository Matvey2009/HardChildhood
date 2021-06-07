from modules.Interface.MiniMap import MiniMap
from modules.Interface.Bullet import Bullet
from modules.Interface.Life import Life
from modules.Interface.Score import Score
class Interface(object):

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.minimap = MiniMap(self.size)
        self.bullet = Bullet(size)
        self.life = Life()
        self.score = Score(size)

    def update(self, hero):
        """Обновление"""
        self.minimap.update(hero)
        self.bullet.update(self.size)
        self.life.update()
        self.score.update(self.size)

    def draw(self, g):
        """Отрисовка"""
        self.minimap.draw(g)
        self.bullet.draw(g)
        self.life.draw(g)
        self.score.draw(g)