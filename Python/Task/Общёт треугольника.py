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
    print("Гипотенуза Треугольника -", math.sqrt(a**2+b**2))
    print("Площядь треуголяника -", a * b / 2)
    print("Периметр треуголяника -", a + b + math.sqrt(a**2+b**2))
    input()