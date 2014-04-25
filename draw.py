# author: skierdude101
length = 100
n=180
angle = 180-180*(n-2)/n
spiral=10
line=1
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

for cat in cats:
	jose.forward(2)
	jose.left(angle)
	