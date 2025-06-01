p = "3"*68
while "999" in p or "333" in p:
	if "333" in p:
		p = p.replace("333", "9", 1)
	else:
		p = p.replace("999", "3", 1)
print(p)
