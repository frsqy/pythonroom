# author: skierdude101
length = 30
n=18
angle = 180-180*(n-2)/n
spiral=10
line=1
colors = ["red","orange","yellow","green","blue","magenta","red","orange","yellow","green","blue","magenta","red","orange","yellow","green","blue","magenta"]
cats=range(0,n)
import turtle

jose = turtle.Turtle()

#jose.forward(100)
#jose.left(90)
#jose.forward(100)
#jose.left(90)
#jose.forward(100)
#jose.left(90)
#jose.forward(100)

jose.color("red")

for color in colors:
	jose.color(color)
	jose.forward(length)
	jose.left(angle)
	