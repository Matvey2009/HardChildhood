print('Введите число "a"')
a = float(input())
print('Введите число "b"')
b = float(input())
print('Введите число "c"')
c = float(input())
de = b * b - 4 * a * c;
if (a == 0):
    print("Один корень: ", -c / b)
elif (de == 0):
    print("Один корень: ", -b / (2*a))
elif (de > 0):
    print("Первый корень: ", (-b + de**0.5) / (2 * a));
    print("Второй корень: ", (-b - de**0.5) / (2 * a));
else:
    print('Корней нет')
input()