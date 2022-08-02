print("Введите число")
n = int(input())
j = 1
s = 0
if (n < 0 or n == 10000000000000000):
    print("Введите корректные данные")
else:
	while(n >= j):
		j *= 2
		s += 1
	print(s)
