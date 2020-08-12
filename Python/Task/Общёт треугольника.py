#Общёт треуголяника
import os
import math
while True:
    os.system("cls||clear")
    print("      _ _             _ _      ")
    print("     |   |           |   |     ") 
    print("     |_ _|           |_ _|     ") 
    print("                               ") 
    print("  _ _                     _ _  ") 
    print(" |   |_ _ _ _ _ _ _ _ _ _|   | ") 
    print(" |_                         _| ") 
    print("   | _ _ _ _ _ _ _ _ _ _ _ |   ") 
    print("                               ") 
    a = int(input("Ведите первое число\n"))
    b = int(input("Ведите второе число\n"))
    с = math.sqrt(a**2+b**2)
    print("Гипотенуза Треугольника -", с)
    print("Площядь треуголяника -", a * b / 2)
    print("Периметр треуголяника -", a + b + с)
    input()