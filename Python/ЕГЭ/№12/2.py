p = "8"*69
while "3333" in p or "8888" in p:
	if "3333" in p:
		p = p.replace("3333", "88", 1)
	else:
		p = p.replace("8888", "33", 1)
print(p)
