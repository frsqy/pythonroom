import turtle

new = turtle.Turtle()

colors=["00FFF7","00FF00","FF70D2","FF2424","3124E6"]
pentagon=72
pentalength=50
for color in colors:
	new.color(color)
	new.forward(pentalength)
	new.left(pentagon)
	