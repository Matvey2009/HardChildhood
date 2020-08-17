#Расчёт эпитента взрыва

import math

    print("      _ _             _ _      ")
    print("     |   |           |   |     ") 
    print("     |_ _|           |_ _|     ") 
    print("                               ") 
    print("  _ _                     _ _  ") 
    print(" |   |_ _ _ _ _ _ _ _ _ _|   | ") 
    print(" |_                         _| ") 
    print("   | _ _ _ _ _ _ _ _ _ _ _ |   ") 
    print("                               ") 

x2 = int(input("Ваши кординаты по x - "))
y2 = int(input("Ваши кординаты по у - "))

x1 = int(input("Кординаты взрыва по х - "))
y1 = int(input("Кординаты взрыва по у - "))

x = x1 - x2
y = y1 - y2
g = math.hypot(x, y)

print("Растояние для взрыва", g)

if g < 5000:
    print("Вы в эпиценре взрыва")
else: 
    print("Вы в бехопасности ")

input()