function abc(text)
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

function num(text)
	print("Количество символов в тексте: "..#text)
end

function probel(text)
	maxi = 0
	space = ''
	for i = 1, #numsym do 
		if numsym[i] > maxi then
			maxi = numsym[i]
			space = origsym[i]
		end
	end
	print("Пробел это: "..space.." | Всего пробелов: "..maxi)
end

--Р’С‹Р±РѕСЂ СЃР»РѕРІ СЃ РїРѕРІС‚РѕСЂРµРЅРёРµРј--
 --РћРґРЅР° Рё РґРІСѓР±С‹РєРІРµРЅС‹С… СЃР»РѕРІ--