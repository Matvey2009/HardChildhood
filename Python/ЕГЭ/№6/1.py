from turtle import *
lt(90)
screensize(2000, 2000)
size = 30
tracer(0)
down()
for i in range(4):
	fd(14*size)
	rt(120)
up()
for x in range(-20, 20):
	for y in range(-20, 20):
		setpos(x*size, y*size)
		dot(4, "red")
done()
