X = int(input())
Y = 1
for i in range(48):
    Y = Y * (i+1)
    if Y == X:
        Y = i+1
        break
print(Y)

#ПЯТАЯ
#Факториалом числа n называют последовательное произведение всех чисел от 1 до n и обозначают n!. Например, 5! = 1 * 2 * 3 * 4 * 5 = 120. 
#Напишите программу, которая из n! получает n.
#Входные данные: n! - факториал числа n
#Выходные данные: n - исходное число
#Пример входных данных: 120
#Пример выходных данных: 5