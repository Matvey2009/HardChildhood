from abc import ABC, abstractmethod


class Abstract(ABC):
    """Абстракный класс для юнитов"""

    scroll_line = 10
    scroll = round(scroll_line / 1.4)

    @abstractmethod
    def update(self):
        """ Обнавление """
        pass

    @abstractmethod
    def draw(self):
        """ Отрисовка """
        pass

    def pos_unit(self, turn):
        """Позиция юнита"""
        if turn == 'right_down':
            self.point_x -= self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_down':
            self.point_x += self.scroll
            self.point_y -= self.scroll
        elif turn == 'left_up':
            self.point_x += self.scroll
            self.point_y += self.scroll
        elif turn == 'right_up':
            self.point_x -= self.scroll
            self.point_y += self.scroll
        elif turn == 'right':
            self.point_x -= self.scroll_line
        elif turn == 'down':
            self.point_y -= self.scroll_line
        elif turn == 'left':
            self.point_x += self.scroll_line
        elif turn == 'up':
            self.point_y += self.scroll_line
        return self.point_x, self.point_y
