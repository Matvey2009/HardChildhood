--     29.01.2022     --
--Программа кодировщик--

os.setlocale('rus_rus.1251')
print('Исходный текст:')
--text = io.read()--
text = [[
Не тот текст
]]

codetext = ""
origsim = {}
codesim = {}
math.randomseed(os.time())

function rnd()
	r = string.char(math.random(14, 127))
	for i = 1, #codesim do
		if r == codesim[i] then
			rnd()
		end
	end
	return r
end

for i = 1, #text do 
	c = string.lower(text: sub(i, i))
	temp = 0
	for j = 1, #origsim do
		if c ~= origsim[j] then
			temp = temp + 1
		elseif c == origsim[j] then
			codetext = codetext .. codesim[j]
			break
		end
	end
	if temp == #origsim then
		origsim[#origsim + 1] = c
		r = rnd()
		codesim[#codesim + 1] = r
		codetext = codetext .. r
	end
end

print(codetext)

io.read()