import shelve


class Save(object):
    """Сохранение и загрузка"""
    def __init__(self):
        path = 'save/save_00'
        self.file = shelve.open(path)
        self.value = 5

    def __del__(self):
        self.file.close()

    def save(self, value):
        self.value = value
        self.file.data = self.value
        print('Сохране...')

    def load(self):
        self.file.date = self.value
        print('Загрузка')
        return self.value