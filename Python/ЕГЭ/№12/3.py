p = "1"*81
while "1111" in p or "88888" in p:
	if "1111" in p:
		p = p.replace("1111", "888", 1)
	else:
		p = p.replace("88888", "888", 1)
print(p)
