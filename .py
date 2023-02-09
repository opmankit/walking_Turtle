import turtle
import random
a = turtle.Turtle()
colors = ['red','brown','green','blue','black']

direction = [0,90,180,270]
for i in range(200):
    a.pensize(5)
    a.forward(30)
    a.speed(30)
    a.color(random.choice(colors))

    a.setheading(random.choice(direction))
