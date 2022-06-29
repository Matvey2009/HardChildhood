print("Введите время прихода первого человека")
h1, m1 = map(int, input().split(':'))
print("Введите время прихода второго человека")
h2, m2 = map(int, input().split(':'))
if (h1 > 23 or h2 > 23 or m1 > 59 or m2 > 59 or h1 < 0 or h2 < 0 or m1 < 0 or m2 < 0):
    print("Введены некорректные данные")
else:
    t = abs((h1 * 60 + m1) - (h2 * 60 + m2))
    if (t < 15 or t > 1425):
        print("Встреча состоялась")
    else:
        print("Всреча не состоялась")
input()