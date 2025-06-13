import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 1
	elif n > 1:
		return n-2+F(n-1)
print(F(2023)-F(2021))

