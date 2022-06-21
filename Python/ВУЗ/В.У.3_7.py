print("Выберите каким вариантов вы хотите высчитать площадь треугольника")
print("1 - Через длины")
print("2 - Через Вершины")
Vibor = int(input())
if (Vibor == 1): 
    print("Введите стороны треугольника")
    a = float(input())
    b = float(input())
    c = float(input())
    
    if (a > b+c or b > a+c or c > a+b):
        print("Ошибочный ввод")
    else:
        p = (a + b + c) / 2;
        S = (p*(p-a)*(p-b)*(p-c))**0.5
        print("S =", S)

elif (Vibor == 2): 
    print("Введите коордитаны вершин треугольника")
    Ax, Ay = map(float, input().split())
    Bx, By = map(float, input().split())
    Cx, Cy = map(float, input().split())
    S = abs(((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)) / 2)
    if (S > 0):
        print("S = ", S)
    else:
        print("Ошибочный ввод")
else:
    print("Ошибочный ввод")
input()
