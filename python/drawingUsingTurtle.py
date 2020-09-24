"""
import turtle
skk= turtle.Turtle()
for i in range(8):
	skk.forward(80)
	skk.right(90)

turtle.done()

"""

import turtle
star = turtle.Turtle()

for i in range(50):
	star.forward(50)
	star.right(144)
turtle.done()


"""

import turtle #outside _IN
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
		for i in range(4):
			skk.fd(size)
			skk.left(90)
			size = size-5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)



"""
"""
import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
colors = ['red' , 'blue' , 'green' , 'orange' , 'yellow']
t = turtle.Pen()
turtle.bgcolor('light blue')
for i in range(200)
	t.circle(5*i)
	t.circle(-5*i)
	t.left(i)
turtle.exitonclick()

"""

"""

import turtle

colors = ['red' , 'purple','blue','green', 'cyan','yellow','white','lime']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(500):
	t.pencolor(colors[x%8])
	t.width(x/100 + 2)
	t.forward(x*5)
	t.right(200)

"""
"""

import turtle
ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
	ninja.forward(100)
	ninja.right(30)
	ninja.forward(20)
	ninja.left(60)
	ninja.forward(50)
	ninja.right(30)
	ninja.penup()
	ninja.setposition(0,0)
	ninja.right(2)
turtle.done()
"""