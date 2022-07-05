print("Введите 5 чисел")
s, l1, r1, l2, r2 = map(int, input().split());
if (abs(s) >= 1e15 or abs(l1) >= 1e15 or abs(r1) >= 1e15 or abs(l2) >= 1e15 or abs(r2) >= 1e15 or l1 >= r1 or l2 >= r2):
    print("Некорректный ввод")
else:
    if (l1 + l2 > s or r1 + r2 < s):
        print(-1)
    else:
        if (s-l1 < r2):
            x1 = l1
            x2 = s - x1
        else:
            x2 = r2
            x1 = s - r2
        print(x1, x2)
input()