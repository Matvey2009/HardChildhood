import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['START', 'OPTIONS', 'LOADING', 'SAFE', 'ADDGAME', 'PROCEED ', '0110101011', 'EXIT']

    def __init__(self, size):
        """ Menu """
        self.menu_state = True
        self.size = size
        self.list_button = []
        for i in range(8):
            btn_pos = self.positon(i)
            button = Button(btn_pos, self.button_name[i])
            self.list_button.append(button)
        self.button_action = None
        self.list_button[6].active = False

    def update(self, e):
        """ Обнавление """
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
            for i in range(8):
                btn_pos = self.positon(i)
                self.list_button[i].rect.x = btn_pos[0]
                self.list_button[i].rect.y = btn_pos[1]

        pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed(3)
        for button in self.list_button:
            if button.active and button.rect.collidepoint(pos):
                button.focus = True
                if click[0]:
                    button.pressed = True
                    self.function(button.name)
                else:
                    button.pressed = False
                    self.button_action = None
            else:
                button.focus = False
            button.update()

    def draw(self, g):
        """ Отрисовка """
        g.fill('black')
        for button in self.list_button:
            button.draw(g)


    def function (self, button_name):
        """ Функции Кнопок """
        if self.button_action != button_name:
            self.button_action = button_name
            if button_name == self.button_name[0]:
                self.menu_state = False
            if button_name == self.button_name[1]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[2]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[3]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[4]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[5]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[6]:
                print('Нажата кнопка', button_name)
            if button_name == self.button_name[7]:
                pg.quit()
                quit()

    def positon(self, i):
        """ Позицыя """
        pos_x = self.size[0] // 2 - 350
        pos_y = self.size[1] // 2 - 200 + i * 120
        if i >= 4:
            pos_x = self.size[0] // 2 + 50
            pos_y = self.size[1] // 2 - 680 + i * 120
        return pos_x, pos_y