import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 1
	elif n >= 2:
		return F(n-1) - G(n-1)
def G(n):
	if n == 1:
		return 1
	elif n>=2:
		return F(n-1)+G(n-1)
print(F(5)/G(5))
