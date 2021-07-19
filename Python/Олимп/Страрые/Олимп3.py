x = int(input())
c = 0
kur = []
while c < x:
    m = input()
    kur.append(m)
    c += 1
for i in kur:
    k = int(i)
    if k <= 100 or (k-100)%7 != 0:
        print(-1)
    else:
        print((k-100)//7)

# Для локального запуска
input()