name, nomer, summa, pol = input().split(',')

if pol == "Ж":
    pol = "ая "
else:
    pol = "ый "
    
nomer = nomer[-4:]

print("Уважаем" + pol + name +  " на вашем счете (карта VISA" + nomer + ") осталось " + summa + " руб.")

#ДЕСЯТАЯ
#Клиенты компании, место работы которых находится на расстоянии R от офиса, должны получить СМС-оповещение. 
#Выведите получит ли СМС наш клиент. 
#Входные данные:  координаты офиса (2 числа),  расстояние R, координаты места работы (2 числа)
#Пример входных данных: 10,12,3,11,12
#Выходные данные: 1 если получит СМС, 0 если нет