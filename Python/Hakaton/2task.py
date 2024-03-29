#ДОРЕШИВАНИЕ
N = int(input())
M = 0
L = 1
R = 1

while N > 0:
    S = R * L * 9
    if N < S:
        M += N // L
        break
    else:
        M += S // L
        N -= S
        R *= 10
        L += 1
print(M)

#ВТОРАЯ
#Книга состоит из N страниц. Известно, что для записи всех номеров страниц этой книги было напечатано M символов.
#Напишите программу, которая вычисляет N из M.
#Входные данные: число символов для записи страниц книги
#Выходные данные: количество страниц в книге
#Пример входных данных: 13
#Пример выходных данных: 11