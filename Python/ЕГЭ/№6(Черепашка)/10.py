from turtle import *
screensize(2500, 2500)
tracer(0)
size = 20
lt(90)
down()
dot(5, "blue")
for i in range(9):
	fd(18*size)
	rt(72)
dot(5, "blue")
up()
for x in range(-100, 100):
	for y in range(-100, 100):
		setpos(x*size, y*size)
		dot(4, "red")
done()
