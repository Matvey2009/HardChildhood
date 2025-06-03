from turtle import *
lt(90)
screensize(2000, 2000)
tracer(0)
size = 30

for i in range(4):
	fd(14*size)
	rt(90)
for j in range(5):
	fd(5*size)
	rt(45)
up()
for x in range(-20, 20): 
	for y in range(-20, 20):
		setpos(x*size, y*size)
		dot(4, "red")
done()
