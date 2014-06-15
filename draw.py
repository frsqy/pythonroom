import turtle

new = turtle.Turtle()

numbers=[1,1000,2]
colors=["00FFF7","00FF00","FF70D2","FF2424","3124E6"]
pentagon=72
pentalength=50

for number in numbers:
	for color in colors:
		new.color(color)
		new.forward(pentalength)
		new.left(pentagon)
	new.left(4)
	