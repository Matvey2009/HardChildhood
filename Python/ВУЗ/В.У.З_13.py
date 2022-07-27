print("Введите число")
n = int(input())
s = "Простое"
if (n < 2 or n > 10000000000):
	print("Введины не коректные данные")
else:
	for i in range(2, n-1):
		if (n % i == 0):
			s = "Составное"
			break
	print("Ответ:", s)
