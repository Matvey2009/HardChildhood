p = "7"*108
while "33333" in p or "777" in p:
	if "33333" in p:
		p = p.replace("33333", "7", 1)
	else:
		p = p.replace("777", "3", 1)
print(p)
