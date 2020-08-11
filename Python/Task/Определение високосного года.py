# Больше - Меньше 

import os

os.system("mode con cols=40 lines=105")

while True:
    x = int(input("Ведите год\n"))
    os.system("cls||clear")
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
input()