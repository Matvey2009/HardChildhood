import mouse
import keyboard
from time import  sleep
from PySide2 import QtCore, QtWidgets
from modules.Form import Ui_Form
import pyautogui as a

class Main(Ui_Form, QtWidgets.QWidget):
    """ Код автокликера """
    def __init__(self):
        super().__init__()
        self.click_x = 0
        self.click_y = 0
        self.setupUi(self)
        self.installEventFilter(self)

        self.show()
        # Сигналы - Слоты
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.autoclick)
        self.click_status = False
        self.pushButton.clicked.connect(self.Button_Click)
        keyboard.hook(self.print_present_key)

    def Button_Click(self):
        """ Переключатель Автоклика """
        self.click_status = not self.click_status
        if self.click_status:
            self.timer.start()
            self.autoclick()
            self.pushButton.setText("Stop")
        else:
            self.timer.stop()
            self.pushButton.setText("Start")

    def autoclick(self):
        """ Автоклик """
        # a.tripleClick()
        for i in range(100):
            mouse.click()
        sleep(0.01)

    def mouseMoveEvent(self, e):
        """ Позицыя курсора """
        self.label_6.setText(str(e.x()))
        self.label_7.setText(str(e.y()))

    # def keyPressEvent(self, e):
       # """ Горячие клавиши(qt) """
       # if e.key():
        # self.label_5.setText(str(chr(e.key())))
       # e.assept()
    def print_present_key(self, e):
        """ Горячие клавиши(keyboard) """
        print(e, e.event_type, e.name)
        if e.event_type == "up":
            self.Button_Click()
