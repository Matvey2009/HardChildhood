import random
o = 1
i = 0
while (o == 1):
	i = 0
	n = 0
	r = random.randrange(0, 100)
	print("Введите своё число, что-бы попытаться угадать загадоное число")
	while (i < 5):
		n = int(input())
		if (n < 0 or n > 100):
			print("Введены некорректные данные")
		i += 1
		if (n == r):
			print("Поздравляю! Вы угадали")
			print("Хотите начать сначала? (1 - ДА )")
			o = int(input())
			break;
		elif (n > r):
			print("Загаданное число меньше")
		else:
			print("Загаданное число больше")
		if (i == 5 and n != r):
			print("Вы проиграли. Было загадано: ", r)
			print("Хотите начать сначала? (1 - ДА )")
			o = int(input())
		elif (n < 0 or n > 100):
			print("Поздравляю! Вы угадали")
			print("Хотите начать сначала? (1 - ДА )")
			o = int(input())
			break;
