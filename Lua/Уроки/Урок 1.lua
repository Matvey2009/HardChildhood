--26.01.2022--

--[[
Многострочные
Коментарии
	]]--
os.setlocale('rus_rus.1251')

io.write('Привет')
print("Привет МИР")--print Преобразовывает в стринг а io.write просто выводит--
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
y = tostring('5') --Преобразовывает число в строку--
print(y)
x, y = y, x
print(x, y)
print(x..y)
a, b, c = 7, 2, 7
print(a..b..c)

print(5^2)--Степень--

x = io.read('*n')
