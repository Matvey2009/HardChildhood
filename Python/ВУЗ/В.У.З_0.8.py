print("Введите уравнение")
num1, word, num2 = input().split()

if (word == "-"):
    print(float(num1) - float(num2))
elif (word == "+"):
    print(float(num1) + float(num2))
elif (word == "/"):
    print(float(num1) / float(num2))
elif (word == "*"):
    print(float(num1) * float(num2))
else:
    print("Введины ошибочные данные")
input()