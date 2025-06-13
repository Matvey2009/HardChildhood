import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return F(n-2)*(n-1)
print(F(8))

