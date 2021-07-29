from random import randint as r


class Units(object):
    """ SuperClass """
    def __init__(self, file):
        """ Конструктор """
        self.file = file
        self.pos = r(20, 400), r(20, 300)

    def console(self):
        print("unit:", self.__class__.__name__)