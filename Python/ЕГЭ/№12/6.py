s=0
for a in range(200, 1000):
	p = a*"1"
	while "1111" in p:
		p = p.replace("1111", "22", 1)
		p = p.replace("222", "1", 1)
	if s < p.count('1'):
		s = p.count('1')
		index = a
print(index)
