# Операторы

x = 5 #input("Ввод в консоль - ")
print("Конвертация в число - ", int(x))
print("Конвертация в дробное число - ", float(x))
print("")

x = "Hello Word"
print("Длина строки - ", len(x))
print("Конвертация в строку - ", str(len(x)) + " - Штук")
print("Транформация в список - ", list(x))
print("Транформация в картеж - ", tuple(x))
print("")

colors = [("Красный", 2), ("Зелёный", 1), ("Синий", 3), ("фиолетовый", 5)]
print("Cписок картежей", colors)
print("Транформация", colors)
colors = dict(colors)
print("")

x = [11, 201, 201, 440, 5, 6, 702, 8, 9, 201]
print("Список", x)
print("Минимальное значение", min (x))
print("Максимальное значение", max(x))
print("Сортировка списка", sorted(x))
print("Обратная сортировка списка", sorted(x, reverse = True))
print("Сумма списка", sum(x))
print("Сумма цифр", sum([1, 2 ,3 ,4 ,5 ,6]))
print("Сумма цикла списка", sum(i ** 2 for i in x))
print("")

print("Набор", set(x))
print("фиксированый набор", frozenset(x))
print("")

print("Bool любого числа", bool(-125))
print("Bool числа 0", bool(0))
print("Bool любого симвала", bool("-125"))
print("Bool пустоты", bool(""))

input()