import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 3
	elif n > 1:
		return F(n-1)*(n-1)
print(F(6))
