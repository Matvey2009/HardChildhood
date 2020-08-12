# Больше - Меньше 

import os

os.system("mode con cols=40 lines=105")

while True:
    print("      _ _             _ _      ")
    print("     |   |           |   |     ") 
    print("     |_ _|           |_ _|     ") 
    print("                               ") 
    print("  _ _                     _ _  ") 
    print(" |   |_ _ _ _ _ _ _ _ _ _|   | ") 
    print(" |_                         _| ") 
    print("   | _ _ _ _ _ _ _ _ _ _ _ |   ") 
    print("                               ") 
    x = int(input("Ведите год\n"))
    os.system("cls||clear")
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
input()