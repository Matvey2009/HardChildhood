--27.01.2022--
os.setlocale('rus_rus.1251')

--  Math  - это библиотека матимотических функцый --
--   os   - это библиотека   системных    функцый --
-- string - это библиотека для работы со строками --
--  table - это библиотека для работы с таблицами -- 


print(string.upper("aaa, BBB"))
print(string.lower("aaa, BBB"))
print(string.gsub('aaaazaaaa', 'z', 'x', 3))
print(string.find("Hello World", 'lo', 1))
print(string.reverse("Hello World"))
print(string.format("Year: % d", 2022))
print(string.char(1))
print(string.byte('abcd', 4))
print(string.byte('abcd'))
print(string.len('Hello World'))
print(string.rep('-=*=- ', 10))

print(math.random()) -- От нуля до единицы --
print(math.random(0, 100)) -- Надо разобраться -- 
print(math.randomseed(0, 100)) -- Надо разобраться --

arr = {2, 9, 15, 19, 56, 20, 11, 48, 3, 43}

print(arr[6])
print(#arr) -- Длина массива --

arr2 = {
Pn = "Monday", 
Wt = "Tuesday",
Sr = "Wednesday"
}
print(arr2.Pn..arr2.Wt)
table.sort(arr)
print(arr)

metaArr = {}

setmetatable(arr, metaArr) -- Элемент находящийся в массиве --

x = io.read('*n')