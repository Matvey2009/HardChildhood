import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	elif n == 3:
		return 1
	elif n > 3:
		return F(n-3) + F(n-2) + F(n-1)
print(F(11))
