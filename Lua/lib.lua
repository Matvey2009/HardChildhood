function abc(text)
	print("Количество символов: "..#text)
	origsym = {}
	numsym = {}
	for i = 1, #text do
		s = text: sub(i, i)
		temp = 0
		for j = 1, #origsym do
			if origsym[j] ~= s then
				temp = temp + 1
			elseif s == origsym[j] then
				break
			end
		end
		if temp == #origsym then
			origsym[#origsym+1] = s
			x = 0
			for n = 1, #text do
				stemp = text: sub(n, n)
				if s == stemp then
					x = x + 1
				end
			end
			numsym[#numsym + 1] = x
		end
	end

	numabc = 0
	for i = 1, #origsym do
		numabc = numabc..origsym[i]..' - '..numsym[i]..', '
	end
	print(numabc)
end