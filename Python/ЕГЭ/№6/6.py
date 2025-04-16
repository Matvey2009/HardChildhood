from turtle import *
lr = 90
screensize = 2000
size = 20
tracer(0)

for i in range(4):
	fd(8*size)
	rt(150)
	fd(8*size)
	rt(30)
up()
for x in range(-20, 20):
	for y in range(-20, 20):
		setpos(x*size, y*size)
		dot(4, "red")
done()
