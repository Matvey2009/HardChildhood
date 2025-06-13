import sys
sys.setrecursionlimit(9999999)
def F(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n % 2 == 0:
		return int((4*n-F(n-3))/8)
	elif n % 2 != 0:
		return int((4*n-F(n-1)+F(n-2))/8)
print(F(52) - F(38))
