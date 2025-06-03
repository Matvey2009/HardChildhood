import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 1
	if n == 2:
		return 3
	if n > 2:
		return F(n-1) *n + F(n-2)*(n-1)
print(F(5))
