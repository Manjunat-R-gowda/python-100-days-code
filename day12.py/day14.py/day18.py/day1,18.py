from turtle import Turtle,Screen

new=Turtle()
def distance_cover():
    new.forward(50)

def disc():
    new.back(50)

def tur():
    new_co=new.heading()+10
    new.setheading(new_co)

def mu():
    new_coo=new.heading()-10
    new.setheading(new_coo)
   
def scc():
    new.clear()
    new.reset()




    
screen=Screen()
screen.listen()
screen.onkey(key="w",fun=distance_cover)
screen.onkey(key="s",fun=disc)
screen.onkey(key="a",fun=tur)
screen.onkey(key="d",fun=mu)
screen.onkey(key="c",fun=scc)
screen.exitonclick()