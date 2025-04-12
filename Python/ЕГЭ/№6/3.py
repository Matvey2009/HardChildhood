from turtle import *
size = 30
lt(90)
screensize(2000, 2000)
tracer(0)
for i in range(4):
	fd(12*size)
	rt(90)
rt(30)
for j in range(3):
	fd(8*size)
	rt(60)
	fd(8*size)
	rt(120)
up()
for x in range(-20, 20):
	for y in range(-20, 20):
			setpos(x*size, y*size)
			dot(4, "red")
done()
