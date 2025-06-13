import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return n
	elif n > 1:
		return F(n-1)*(n+2)
print(F(5))
