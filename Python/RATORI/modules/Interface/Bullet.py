import pygame as pg


class Bullet(object):
    """Пули"""
    pg.init()

    def __init__(self, size):
        """Конструктор"""
        self.size = size
        self.bullet = 7
        self.font = pg.font.Font(None, 36)
        self.text = self.font.render(str(self.bullet), True, 'Black')
        self.sound_reload = pg.mixer.Sound("sounds\Reload.mp3")
        self.sound_shots = pg.mixer.Sound("sounds\Shots.mp3")
        self.sound_shots2 = pg.mixer.Sound("sounds\Shots2.mp3")
        self.step = 0

    def update(self, size):
        """Обновление"""
        keysM = pg.mouse.get_pressed()
        keysK = pg.key.get_pressed()
        size = pg.display.get_window_size()
        if self.size != size:
            self.size = size
        if self.step < 8:
            self.step += 1
        else:
            self.text = self.font.render(str(self.bullet), True, 'Black')
            if keysM[0]:
                self.Shot()
                self.text = self.font.render(str(self.bullet), True, 'Black')
            if keysK[pg.K_r]:
                self.Reload()
                pg.mixer.Sound.play(self.sound_reload)
                self.text = self.font.render('Reload', True, 'Black')


    def Shot(self):
        self.step = 0
        if self.bullet > 0:
            pg.mixer.Sound.play(self.sound_shots)
            self.bullet -= 1
        else:
            pg.mixer.Sound.play(self.sound_shots2)
            self.bullet = 0

    def Reload(self):
        self.step = 0
        self.bullet = 7
        self.update(self.size)

    def draw(self, g):
        """Отрисовка"""
        g.blit(self.text, (self.size[0]-100, self.size[1]-50))