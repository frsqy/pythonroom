# author: skierdude101
length = 6
n=13
numbers = range(1,1000,10)
#angle = 180-180*(n-2)/n
spiral=10
line=1
#colors = ["red","orange","yellow","green","blue","magenta","red","orange","yellow","green","blue","magenta","red","orange","yellow","green","blue","magenta"]
#colors = ["red", "orange", "yellow", "green"]
colors = ["red","orange","yellow","green"]
#cats=range(0,n)
import turtle

jose = turtle.Turtle()

#jose.forward(100)
#jose.left(90)
#jose.forward(100)
#jose.left(90)
#jose.forward(100)
#jose.left(90)
#jose.forward(100)

#jose.color("red")

#for color in colors:
#	jose.color(color)
#	jose.forward(length)
#	jose.left(angle)
#for color in colors:
#	jose.forward(100)
#	jose.left(170)
#for cat in cats:
#	jose.forward(50)
#	jose.left(angle)
for number in numbers:
	for color in colors:
		jose.color(color)
		jose.forward(number)
		jose.left(90)
	jose.left(4)
	