#

import random
import math
import os

name = ["......", "Камень", "Ножнецы", "Бумага"]
Game = 0
Win  = 0
Draw = 0
Loss = 0

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

    print("1 - камень, 2 - ножницы, 3 - бумага")
    Player = int(input("Ведите число\n"))
    os.system("cls||clear")
    print("Вы выбрали -", name[Player])
    Bot = random.randint(1,3)
    print("Компьютер выбрал -", name[Bot])
    Game += 1
    if Player == Bot:
        print("Ничья")
        Draw += 1
    elif (Player == 1 and Bot == 2) or (Player == 2 and Bot == 3) or (Player == 3 and Bot == 1):
        print("Вы победили")
        Win += 1
    else:
        print("Вы проиграли")
        Loss += 1
    
    print("Побед", Win )
    print("Ничья", Draw)
    print("Поражений", Loss)
    print("Всего игр", Game)
input()