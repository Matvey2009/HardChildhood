N = int(input())

if N < 10:
    M = N    
else:
    M = (N - 9) + N * 2

print(M)

#ВТОРАЯ
#Книга состоит из N страниц. Известно, что для записи всех номеров страниц этой книги было напечатано M символов.
#Напишите программу, которая вычисляет N из M.
#Входные данные: число символов для записи страниц книги
#Выходные данные: количество страниц в книге
#Пример входных данных: 13
#Пример выходных данных: 11