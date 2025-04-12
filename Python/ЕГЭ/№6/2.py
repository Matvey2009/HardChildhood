from turtle import *
screensize(2000, 2000)
size = 30
lt(90)
tracer(0)
down()
for i in range(12):
	rt(60)
	fd(1*size)
	rt(60)
	fd(1*size)
	rt(270)
up()
for x in range(-20, 20):
	for y in range(-20, 20):
		setpos(x*size, y*size)
		dot(4, "red")
done()
