p = "0" + "1"*12 + "2"*15 + "3"*17
while ("01" in p) or ("02" in p) or ("03" in p):
	p = p.replace("01", "20", 1)
	p = p.replace("02", "120", 1)
	p = p.replace("03", "302", 1)
print(p.count("1"))
