#Ввод
N = 10 #input("Диапозон номеров")
M = 7 #input("Количество номеров")
arr = "1 3 6 4 3 2 9" #input("Вводим масив")
arr = arr.split()
setArr = set(arr)

#Решение
sumn = 0
for i in setArr:
    x = arr.count(i)
    if x > sumn:
        maxn = i
        sumn = x
    elif x == sumn and int(maxn) > int(i):
        maxn = i
    
#Вывод
print(maxn, sumn)
input()