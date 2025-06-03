from turtle import * 
screensize = 2000
size = 20
lr = 90
tracer(0)

for a in range(3):
	fd(7*size)
	rt(90)
fd(10*size)
for b in range(3):
	rt(270)
	fd(6*size)
up()
for x in range(-20, 20):
	for y in range(-20, 20):
		setpos(x*size, y*size)
		dot(4, "red")
done()
