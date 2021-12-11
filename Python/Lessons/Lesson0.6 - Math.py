# Математические функции
import math

x = 5
print("Длина строки(123) -", len("123"))
print("Округление(4.5) -", round(4.5))
print("Число PI -", math.pi)
print("Число exeponenta -", math.e)
print("Число возведение в степень(2,3) -", math.pow(2,3))#
print("Число остаток от деления(7, 3) -", math.fmod(7, 3))#
print("Проверка на число(5) -", math.isfinite(x))
print("Проверка на бесконечность(5) -", math.isinf(x))
print("Мантиса и Экспонента(123.456) -", math.frexp(123.456))
print("Мантиса и Экспонента(123.456) -", math.frexp(123.456))
print("Квадратныйы корень(9) -", math.sqrt(9))
print("Модуль(-20) -", math.fabs(-20))
print("Модуль числа 1, с знаком числа 2(-10, 5) -", math.copysign(-10, 5))
print("Отделяет целую часть и дробную(123.456) -", math.modf(123.456))
print("Деление и остаток", divmod(10,3))
print("Округление в большую сторону(4.1) -", math.ceil(4.1))
print("Округление в меньшую сторону5.9) -", math.floor(5.9))
print("Отбрасывает дробную часть(5.9) -", math.trunc(5.9))
print("Косинус угла(60) -", math.cos(math.radians(60)))
print("Синус угла(30) -", math.sin(math.radians(30)))
print("Синус угла(45) -", math.tan(math.radians(45)))
print("Гипотинуза(10, 20) -", math.hypot(10, 20))
print("Логарифм(8, 2) -", math.log(8, 2))
print("Логарифм10(100) -", math.log10(100))

input()