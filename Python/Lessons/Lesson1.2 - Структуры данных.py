# Урок № 12 по Python - структуры данных STR / INT - LIST

"******************************************************************************"

print("   === ТРАНСФОРМАЦИЯ ИЗ СТРОКИ С БУКВАМИ ===")

print(" -= 1. Строка в список по буквам =-")
def STR_LIST(x):
    print("Тип:", type(x), "на входе: ", x)
    res = list(x)
    return res
x = "Hello World!"
res = STR_LIST(x)
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print()

print(" -= 2. Строка в список по разделителю =-")
x = "Hel, lo, Wor, ld, !"
print("Тип:", type(x), "на входе: ", x)
res = x.split(", ")
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print()

print(" -= 3. Строка в список с форматированием =-")
x = "Hello World!"
print("Тип:", type(x), "на входе: ", x)
res = list(map(str.upper, x))
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print()

print(" -= 4. Строка в список по разделителю с форматированием =-")
x = "Hello World!"
print("Тип:", type(x), "на входе: ", x)
res = list(map(str.swapcase, x.split(" ")))
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print("\n")

"******************************************************************************"

print("   === ТРАНСФОРМАЦИЯ ИЗ СТРОКИ С ЧИСЛАМИ ===")

print(" -= 5. Строка в список цифр =-")
x = "12345"
print("Тип:", type(x), "на входе: ", x)
res = list(map(int, x))
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print()

print(" -= 6. Строка в список чисел =-") # пример для олимпиады 6-1
x = "1 23 456 7890"
print("Тип:", type(x), "на входе: ", x)
res = list(map(int, x.split()))
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print()

print(" -= 7. Строка в список чисел c разделителем =-")
x = "1 - 23 - 456 - 7890"
print("Тип:", type(x), "на входе: ", x)
res = list(map(int, x.split("- ")))
print(type(res), "тип:", type(res[0]), "на выходе: ", res)
print("\n")

"******************************************************************************"

print("   ***** ТРАНСФОРМАЦИЯ ИЗ СПИСКА В СТРОКУ *****")

print(" -= 8. Список строк в строку (конкатанация) =-")
x = ["Hel", "lo ", "Wor", "ld", "!"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "".join(x)
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 9. Список строк в строку с форматированием =-")
x = ["Hel", "lo ", "Wor", "ld", "!"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "".join(map(str.upper, x)) # через карту
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 10. Список строк в строку с разделителем =-")
x = ["Hel", "lo ", "Wor", "ld", "!"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "-".join(x)
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 11. Список строк в строку с разделителем и форматированием =-")
x = ["Hel", "lo ", "Wor", "ld", "!"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "-".join(str.swapcase(i*3) for i in x) # через генератор
print("Тип:", type(res), "на выходе: ", res)
print("\n")

"******************************************************************************"

print("   ***** ТРАНСФОРМАЦИЯ ИЗ СПИСКА В ЧИСЛО *****")

print(" -= 12. Список чисел в строку =-")
x = [1, 23, 456, 7890]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "".join(map(str, x)) # через карту
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 13. Список чисел в число =-")
x = [1, 23, 456, 7890]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = int("".join(map(str, x))) # через карту
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 14. Список чисел в строку с разделителем =-")
x = [1, 23, 456, 7890]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = " ".join(str(i) for i in x) # через генератор
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 15. Список строк чисел в строку =-")
x = ["1", "23", "456", "7890"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "".join(x)
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 16. Список строк чисел в строку с разделителем =-")
x = ["1", "23", "456", "7890"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = "-".join(x)
print("Тип:", type(res), "на выходе: ", res)
print()

print(" -= 17. Список строк чисел в число =-")
x = ["1", "23", "456", "7890"]
print(type(x), "тип:", type(x[0]), "на входе: ", x)
res = int("".join(x))
print("Тип:", type(res), "на выходе: ", res)
print()

input()