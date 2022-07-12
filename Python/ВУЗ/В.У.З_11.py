print('Введите число а затем и степень')
c = int(input())
s = int(input())
g = c
for i in range(s-1):
    g *= s
print(g)
input()