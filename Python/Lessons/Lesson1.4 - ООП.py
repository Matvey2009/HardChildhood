# Урок № 14 по Python - ООП

class Tank():
    life = 0
    speed = 0
    _life = 100 # _ обозначение закрытых полей, __ - еще закрытие
    
    def repair(self, r):
        if self.life < 1:
            self.life = 0
        elif self.life < self._life:
            self.life += r
        if self.life > self._life:
            self.life = self._life
        pass
    
    @staticmethod
    def NoObject():
        print("Статический метод, т.е. без объекта")

T34 = Tank()
T34.life = 100
T34.speed = 30

print("ХП танка Т34 -", T34.life)
print("Скорость Т34 -", T34.speed)
print("Смотрим тип объекта", type(T34))
print()

T34.life -= 50
print("Подбитый танк -", T34.life)
T34.repair(40)
print("Танк после ремонта -", T34.life)
T34.repair(40)
print("Еще один ремонт -", T34.life)
T34.life -= 99.5
T34.repair(40)
print("Ремонт невозможен -", T34.life)
print(T34)
#del T34
Tank.NoObject()
print()
#!--------------------------------------------------------------------------------------------!#
class Scaner(Tank):
    vision = 0
    
    def __init__(self, vision): # конструктор
        self.vision = vision
    
    def __del__(self): # деструктор, срабатывает при удалении
        print("объект удален")

scanT34 = Scaner(500)
print("Новый класс-наследник -", scanT34.vision)
print("Данные от класса-предка -", scanT34._life)
print()

print("смотрим тип объекта", type(scanT34))
print("проверка принадлежности объекта к классу Scaner - ", isinstance(scanT34, Scaner))
print("проверка принадлежности к родительскому классу Tank -", isinstance(scanT34, Tank))
print("проверка принадлежности к чужому классу", isinstance(T34, Scaner))
#del scanT34
print("После удаления не сработает -", scanT34.vision)
print()
#!--------------------------------------------------------------------------------------------!#
class Close_person:
    def __init__(self, name):
        self.__name = name
        self.__age = 0
    
    @property # свойство - геттер
    def age(self):
        return self.__age
    
    @age.setter # свойство - сеттер
    def age(self, age):
        if age in range(0, 150):
            self.__age = age
        else:
            print("Столько не живут")
    
    @property
    def name(self):
        return self.__name
    
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
    
    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)

Mahmud = Close_person("Mahmud")
#Mahmud.display_info()
print(Mahmud)

Mahmud.age = 200
print("Возраст", Mahmud.age)

Mahmud.age = 20
Mahmud.display_info()

input()