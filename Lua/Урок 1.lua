--26.01.2022--

--[[
Многострочные
Коментарии
	]]--
os.setlocale('rus_rus.1251')

io.write('Привет')
print("Привет МИР")
print([[
Привет
Мир...
]])

x = 727
print(x)
print(type(x))
print(type('x'))
print(type(true))
print(type(nil))

--Отынтовка в число--
y = tonumber('5') --Строки всегда конкстанты--
print(y)
x, y = y, x
print(x, y)
print(x..y)
a, b, c = 7, 2, 7
print(a..b..c)

x = io.read('*n')
