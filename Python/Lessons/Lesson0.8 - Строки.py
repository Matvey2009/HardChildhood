# Строки

x = 1234554321
x = str(x)
print("Конфиртация в строку", x)
print("Повторение строки", x * 2)
print("Сровнение строк", "abc" > "x")
print("Сровнение строк", "a" > "B")
print("Код символа", ord("Z"))
print("Поиск позиции смвола в строке", x.find("4"))
print("Точный поиск позиции смвола в строке", x.index("4"))
print("Поиск c конца", x.rfind("4"))
print("Поиск позиции символа в диопозоне", x.find("4", 4, 7))
print("")

print("Замена символа", x.replace("4", "g"))
print("Замена символа", x.replace("5", ""))
print("Замена символов столько сколько надо", x.replace("3", "zzz", 2))
print("")

x = "FFF PPP mmm zzz"
print("В заглавные", x.upper())
print("В пропесные", x.lower())
print("Cюольшёл буквы", x.title())
print("Первое слово с большёл буквы", x.capitalize())
print("")

x = "123454321"
print("Подчёт совпадений", x.count("4"))
print("Подчёт совпадений в диопозоне", x.count("4", 1, 5))
print("Проверка строки на число", x.isdigit())
print("Проверка строки на буквы", x.isalpha())
x = "1 21 321 4321 54321 654321 7654321 87654321 987654321"
print("Конвертация строки в список", x.split())
x = "1, 21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321"
print("Конвертация строки в список с разделителем", x.split(", "))
x = ["a", "b", "c"]
x = "-".join(x)
print("Конвертация список в строки", x)

x = "1 21 125 1254 12547"
print(x)
print(x.ljust(50, "*"))
print(x.rjust(50, " "))
print("Cимвол №7", x[7])
print("Срез от 7 до 12 -", x[7:12])
print("Срез последний символов", x[-5:])
print("Срез первых 10 сиволов", x[:10])
print("Срез символов с шагом 2", x[::2])
x = [1, 2, 3, 4, 5, 6, 7]
del x[3]
print("Удаление подстроки", x)
del x[3:5]
print("Удаление подстроки", x)
x[2] = "Алада-Кидавра"
print("замена подстроки", x)
input()