import sys
sys.setrecursionlimit(9999999)
n=1
def F(n):
	if n == 1:
		return n
	if n > 1:
		return F(n-1)*F(n-1) - F(n-1)*n+2*n
	
print(F(4))
