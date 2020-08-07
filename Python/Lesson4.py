# Цикл

import random

x = 0
while x < 3:
    x += 1
    print(x)
    
GameOver = False
while not GameOver:
    x += 1
    if x > 6:
        GameOver = True
    print(x)

# Циклы For: Stop, Start-Stop, Start-Stop-Step.

for i in range(5):
    print(i)
    
for i in range(10,13):
    print(i)
    
for i in range(100, 200, 20):
    print(i)
    

x = [-15, -10, 100, 1000, 1002]
print(x)
print(type (x))
for i in x:
    print(i)
    
for i in "Hello World":
    print(i)
    
#Цикл в цикле
for i in range(1, 11):
    for j in range(10):
        print(i * j, end = " ")
    print("")
    
#break и continueue
x = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(x)
random.shuffle(x)
print(x)
while True:
    #print("Раном от 0 до 1", random.random())
    #print("Раном от 100 до 200 -", random.randint(100,200))
    #print("Раном-Range до 10 -", random.randrange(10))
    #print("Раном от 1000 до 2000 -", random.randrange(1000, 2000))
    #print("Раном от 90 до 180 c шогом 3-", random.randrange(90, 180, 3))
    #print("Раном из списка", random.choice(x))
    y = input("Выйти - 0|Продолжить - 1")
    if y == "0":
        break
    else:
        continue
input()