# Логика

x = True
y = False
print(x == y)
x = 5
y = 6
z = x == y
print(z)
print(type(z))
print(x != y)
print(x > y)
print(x >= y)

print(x > 0 and y > 0)
print(x < 0 or y < 0)
print(not x == y)

x = 10
if x > 0:
    print("Число", x, "-> 0")
    if x == 10:
        print("Я тут")
elif x == 0:
    print("Число 0")
else:
    print("Число > 0")
    
if 5 < x < 25:
    print("Двоеное сравнение" +  str(x))
    
if x > 0:
    print("Я тут")

print(all([1, 125, "x", "abc", "True", 2 > 1]))
print(any([0, 0, "", "", "", 0 > 1]))
print('да') if 2 > 5 else print('YEN')
if all([5 < 3, 1 > 0, 6 > 2, 0 == 0]):
    print('ДА')
else:
    print('нет')

input()