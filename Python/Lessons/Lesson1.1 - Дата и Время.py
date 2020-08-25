# Урок № 11 по Python - дата и время

import datetime

x = datetime.time(18, 30, 15, 0)
print("Время:", x)
print("Тип данных: ", type(x))
print("час: ", x.hour)
print("минуты: ", x.minute)
print("секунды: ", x.second)
print("микросекунды: ", x.microsecond)
print()

x = datetime.date.today()
print("Сегодня: ", x)
print("Тип данных: ", type(x))
print("год: ", x.year)
print("месяц: ", x.month)
print("день: ", x.day)
print("День недели (0-6): ", x.weekday())
print()

x = datetime.datetime(1961, 4, 12)
print("Сейчас дата и время: ", x)
print("Тип данных: ", type(x))
print("час: ", x.hour)
print("минуты: ", x.minute)
print("День недели (1-7): ", x.isoweekday())
print()

y = datetime.datetime.today()
delta = y - x
print(type(delta))
print("период между датами в днях: ", delta.days)
print("период между датами в секундах: ", delta.total_seconds())
print("сравнение дат: ", y > x)
print()

x = y.year
print("Выборка данных:", x)
print("Формат выборки данных:", type(x))

input()