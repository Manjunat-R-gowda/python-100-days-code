from turtle import Turtle,Screen
from day318 import random_colours

spiro = Turtle()



spiro.speed("fastest")
for _ in range(100):

    spiro.pensize(10)
    spiro.color(random_colours)
    spiro.circle(100)
    spiro.setheading(spiro.heading()+10)

screen=Screen()
screen.exitonclick()