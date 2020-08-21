# Функции

def main():
    HW()
    HW_name("Матвей")
    HW_name_pluss("Test")
    HW_name_pluss()
    Name_age("Матвей1", 11)
    Name_age(11, "Матвей2")
    Name_age(name = "Матвей3", age = 11)
    Name_age(age = 11, name = "Матвей4")
    Summ(1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    x = Summ_return(1, 2, 3)
    print("Сумма -", x)
    Name, Age = Return_lot()
    print(Name, Age)
    print(Return_lot())

# Простая функция
def HW():
    print("Hello Word")
    print("")

# функция с параметром
def HW_name(x):
    print("Привет", x)
    print("")

# функция с параметром по умолчанию
def HW_name_pluss(x = "Пользаватель"):
    print("Привет", x)
    print("")

# функция с имменовоными параметроми
def Name_age(name, age):
    print("Имя -", name, "Возраст -", age)
    print("")
    
# функция с множеством параметров параметров
def Summ(*params):
    S = 0
    for i in params:
        S += i
    print("Сумма -", S)
    print("")

# функция с возвратом
def Summ_return(*params):
    S = 0
    for i in params:
        S += i
    return S
    
# функция с несколькоми возвратом
def Return_lot():
    name = "Алада_Кидавра -"
    age = 11
    return name, age
    
# функция с несколькоми возвратом
def Return_lot():
    name = "Алада_Кидавра -"
    age = 11
    return name, age

main()

input()