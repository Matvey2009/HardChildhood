k = 0
import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n < 10:
		return n
	elif n >= 10:
		return F(n%10)+F(n//10)
for i in range(2**63):
	if F(i) == 159:
		k += 1


#Определите количество значений n, меньших 263, для которых F(n) = 159
#https://inf-ege.sdamgia.ru/problem?id=62468
