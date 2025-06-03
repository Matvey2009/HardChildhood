from turtle import *
screensize(2500, 2500)
tracer(0)
size = 20
lt(90)
dot(10, "blue")
for a in range(11):
	fd(36*size)
	rt(72)
dot(10, "blue")
up()
for x in range(-15, 60):
	for y in range(-15, 60):
		setpos(x*size, y*size)
		dot(4, "red")
dot(10, "blue")
done()
