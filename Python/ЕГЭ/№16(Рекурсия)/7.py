import sys
sys.setrecursionlimit(9999999)
n=0
def F(n):
	if n == 0:
		return 0
	elif n>0 and n % 3 == 2:
		return F(n-1)+1 
	elif n > 0 and n % 3 < 2:
		return F((n-n%3)/3)
while F(n) != 6:
	n+=1
print(n)
