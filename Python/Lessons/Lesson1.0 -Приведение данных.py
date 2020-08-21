# Конвиртация данных

# int - int - int
def int_int_int(x):
    print("Ввод: ", x, " - Тип данных", type(x))
    res = x*2
    return res

res = int_int_int(100)
print("Вывод: ", res, " - Тип данных", type(res))
print()

# str-str-str
x = "20"
print("Ввод: ", x, " - Тип данных", type(x))
res = x+x
print("Вывод: ", res, " - Тип данных", type(res))
print()

# int-int-str
x = 380
print("Ввод: ", x, " - Тип данных", type(x))
res = str(x//10)+" Попугаев"
print("Вывод: ", res, " - Тип данных", type(res))
print()

# int-str-str
x = 123
print("Ввод: ", x, " - Тип данных", type(x))
res = str(x)[::-1]
print("Вывод: ", res, " - Тип данных", type(res))
print()

# int-str-int
x = 123
print("Ввод: ", x, " - Тип данных", type(x))
res = int(str(x)[::-1])
print("Вывод: ", res, " - Тип данных", type(res))
print()

# str-str-int
x = "12345"
print("Ввод: ", x, " - Тип данных", type(x))
res = int(str(x+x))
print("Вывод: ", res, " - Тип данных", type(res))
print()

# str-int-str
x = "654"
print("Ввод: ", x, " - Тип данных", type(x))
res = str(int(x)*2)
print("Вывод: ", res, " - Тип данных", type(res))
print()

# str-int-int
x = "654"
print("Ввод: ", x, " - Тип данных", type(x))
res = int(x)//2
print("Вывод: ", res, " - Тип данных", type(res))
print()

input()