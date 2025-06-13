import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n <= 2:
		return n + 1
	elif n > 2:
		return F(n-1)+ 3*F(n-2)
print(F(4))

