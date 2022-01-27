--27.01.2022--
os.setlocale('rus_rus.1251')

x = 5
repeat
	print('Repeat ', x)
	x = x - 1
until x < 0

print()

while x < 5 do
	x = x + 1
	print('While ', x)
end

print()

for i = 1, 5, 2 do 
	print('For ', i)
end

print()

-- Eterator --
arr = {5, 10, 15, 20, 25}
for k, i in ipairs(arr) do
	print('ipairs ', k.." "..i)
end

print()

for i = 1, #arr do
	print('Fortwo ', arr[i])
end

-- Запуск файла --
--dofile("D:\Documents\Programs\HardChildhood\Lua")--

--local module = require("Main")


x = io.read('*n')