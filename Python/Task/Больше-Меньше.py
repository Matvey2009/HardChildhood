#Больше-Меньше

import random

print("Здравствуйте, это игра 'Больше-меньше' сдесь компьютер загадывает Любое число от 1 до 1000 а, вы должны его отгодать")

Bot = random.randrange(0, 1000)
while True:
    Player = int(input("Ваше число\n"))

    if Bot == Player:
        print("Вы победили")
    if Player < Bot:
        print("Число больше")
    if Player > Bot:
        print("Число меньше")

input()