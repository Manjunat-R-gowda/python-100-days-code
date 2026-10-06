from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(500,400)
user_choice=screen.textinput(title="make your bet", prompt="what is the colour of the turtle ")
print(user_choice)


colours=["red","orange","blue","green","yellow","purple"]
all_random=[]
coridinates=[-100,-70,-50,20,50,80]


for turtle_index in range(0,5):
    new=Turtle(shape="turtle")
    
    new.penup()
    new.color(colours[turtle_index])
    new.goto(-230,coridinates[turtle_index])

    all_random.append(new)

if user_choice:
    user_is=True

while user_is:
    for turtle in all_random:
        if turtle.xcor()>230:
            user_is=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_choice:
                print(f"you win the colour is {winning_colour} ")
            else:
                print(f"you loose the winning colour is {winning_colour}")
        all_ch=random.randint(0,10)
        turtle.forward(all_ch)

























screen.exitonclick()