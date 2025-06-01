p = "1"*80
while "11111" in p:
	p = p.replace("111", "2", 1)
	p = p.replace("222", "1", 1)
print(p)
