x = int(input())
c = 0
kur = []
while c < x:
    m = input()
    kur.append(m)
    c += 1
for i in kur:
    k = int(i)
    k = (k-100)//7
    print(k)

# Для локального запуска
input()