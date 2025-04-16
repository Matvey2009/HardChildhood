from turtle import *
screensize(2000, 2000)
size = 20
lr = 90
tracer(0)

for a in range(2):
	fd(21*size)
	rt(90)
	fd(27*size)
	rt(90)
up()
fd(9*size)
rt(90)
fd(10*size)
rt(270)
down()
for b in range(2):
	fd(86*size)
	rt(90)
	fd(47*size)
	rt(90)
up()
for x in range(-45, 45):
	for y in range(-45, 45):
		setpos(x*size, y*size)
		dot(4, "blue")
done()
