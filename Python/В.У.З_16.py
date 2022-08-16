t = int(input())
k = "1"
for i in range(t):
	s = 0
	k = "1"
	n, a = map(int, input().split())
	for j in range(n-1):
		k += "1"
	k = str(int(k)*a)
	for j in k:
		s += int(j)
	print(s)
