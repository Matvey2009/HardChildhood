# Yrock 9

x = "Hello world!"
print("Конвертация строки в массив -", list(x))
x = []
print("Моздание пустого списка -", x)
x.append(123)
x.append(456)
print("Добавляем в конец списка -", x)
y = ["abc", "deg"]
print("Создание списка с данными -", y)
x.extend(y)
print("Добавляем список в cписок -", x)
x.insert(2, "000000")
print("Вставляем элемент в позицию cписка -", x)
x.append(123)
x.remove(123)
print("Удаляем один элемент из cписка -", x)
x.pop(1)
print("Вырезаем позицию с элементом из cписка -", x)
y = x.copy()
print("Копируем список (не ссылку) -", y)
y.clear()
print("Очищаем список -", y)
print()

print("Ищем позицию элемента -", x.index(456))
print("Ищем позицию элемента от позиции -", x.index(123, 2))
print("Ищем позицию элемента в диапазоне -", x.index("abc", 1, 4))
print("Подсчет совпадений в списке -", x.count(123))
print()

x = [1, 3, 5, 10, 2]
x.sort()
print("Сортировка списка -", x)
x.reverse()
print("Переворот списка -", x)
print()

print("Срез списка от ... -", x[2:])
print("Срез списка до ... -", x[:2])
print("Срез списка от и до -", x[1:3])
print("Срез списка от и до с шагом -", x[::2])
print()

for i in x:
    print("Обход списка циклом -", i)

for i in range(len(x)):
    print("Индекс списка -", i, " и его значение - ", x[i])
print()

x = [i * 3 for i in "Hello"]
print("Генератор списка циклом -", x)
x = [i * 4 for i in "Hello" if i != "l"]
print("Генератор списка циклом с условием -", x)

arrName = ['Maxim', 'Nikita', 'Matvey']
arrAge = [16, 14, 12]
arrYear = [2005, 2007, 2009]
arr = list(zip(arrName, arrAge, arrYear))

for Name, Age, Year in zip(arrName, arrAge, arrYear):
    print(Name, Age, Year)

a, b, c = zip(*arr)
print(a)
print(b)
print(c)
    
print(*arr)
input()