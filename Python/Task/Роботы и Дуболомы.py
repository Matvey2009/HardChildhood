arr = []
n = int(input())
for i in range(n): 
	p = input()
	x = y = 0
	arr = [[x, y]]
	k = "kiborg"
	for j in range(0, len(p), 2):
		t = p[j:j+2:]
		if (t == "00"):
			y += 1
		elif (t == "01"):
			x += 1	
		elif (t == "10"):
			x -= 1
		else:
			y -= 1
		if [x, y] in arr:
			k = "robot"
		else:
			arr.append([x, y])
	print(len(arr), k)
