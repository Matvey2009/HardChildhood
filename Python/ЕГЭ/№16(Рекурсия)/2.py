import sys
sys.setrecursionlimit(999999999)

def F(n):
	if n == 1:
		return n
	else:
		return n - 1 + F(n-1)
print(F(2024) - F(2022))
