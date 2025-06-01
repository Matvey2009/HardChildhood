p = "8"*68
while "222" in p or "888" in p:
	if "222" in p:
		p = p.replace("222", "8", 1)
	else:
		p = p.replace("888", "2", 1)
	print(p)
print(p)
