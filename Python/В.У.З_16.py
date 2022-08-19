for i in range(int(input())):
	n, a = map(int, input().split())
	print(sum(map(int, str(int('1'*len(str(a)))*a))) + int(str(int('1'*(len(str(a))+2))*a)[len(str(int('1'*(len(str(a))+2))*a))//2])*(n - len(str(a))))
