import turtle as t
from turtle import Screen
import random

#ndw_project=t.Turtle()
spiro=t.Turtle()
t.colormode(255)

#colour=["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def random_colours():
    r=random.randint(0,250)
    y=random.randint(0,250)
    b=random.randint(0,250)
    random_colours=(r ,y ,b)
    return random_colours

for _ in range(50):
    spiro.color(random_colours())
    spiro.circle(100)
    spiro.setheading(spiro.heading()+10)
    

'''angle=[0,90,180,270]
ndw_project.speed("fastest")

ndw_project.pensize(15)
for _ in range(200):
    ndw_project.color(random_colours())
    ndw_project.forward(30)
    ndw_project.setheading(random.choice(angle))
    
    
screen=Screen()
screen.exitonclick()'''