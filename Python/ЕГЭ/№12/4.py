for a in range(0,35):
	for b in range(0,35):
		for c in range(0,35):
			p = '0' + a*"1" + b*"2" + c*"3" + "0"
			while "00" not in p:
				p = p.replace("01", "210", 1)
				p = p.replace("02", "3101", 1)
				p = p.replace("03", "2012", 1)
			if p.count("1") == 70 and p.count("2") == 56 and p.count("3") == 23:
				print(a+b+c+2)
				break
	print(1)
