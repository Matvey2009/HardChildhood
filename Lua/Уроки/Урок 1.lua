--26.01.2022--

--[[
�������������
����������
	]]--
os.setlocale('rus_rus.1251')

io.write('������')
print("������ ���")--print ��������������� � ������ � io.write ������ �������--
print([[
������
���...
]])

x = 727
print(x)
print(type(x))
print(type('x'))
print(type(true))
print(type(nil))

--��������� � �����--
y = tonumber('5') --������ ������ ����������--
y = tostring('5') --��������������� ����� � ������--
print(y)
x, y = y, x
print(x, y)
print(x..y)
a, b, c = 7, 2, 7
print(a..b..c)

print(5^2)--�������--

x = io.read('*n')
