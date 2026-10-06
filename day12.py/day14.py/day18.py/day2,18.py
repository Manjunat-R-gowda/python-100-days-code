from turtle import Turtle,Screen

new_pro=Turtle()



def trai():
    for _ in range(3):
        new_pro.color("yellow")
        new_pro.forward(100)
        new_pro.right(-120)
        new_pro.right(-120)
        

def all_angles():
    for _ in range(4):
        new_pro.color("red")
        new_pro.forward(100)
        new_pro.right(90)
        

def pent():
    all_angles()
   

       
    for _ in range(5):
        new_pro.color("green")
        new_pro.forward(100)
        new_pro.right(72)
        

def hex():
    for _ in range(6):
        new_pro.color("grey")
        new_pro.forward(100)
        new_pro.right(60)

def hept():
    for _ in range(7):
        new_pro.color("black")
        new_pro.forward(100)
        new_pro.right(51.42)

def oct():
        for _ in range(8):
            new_pro.color("blue")
            new_pro.forward(100)
            new_pro.right(45)

def deca():
        for _ in range(10):
            new_pro.color("pink")
            new_pro.forward(100)
            new_pro.right(36)




    




trai()
all_angles()

pent()
hex()
hept()
oct()
deca()










screen=Screen()
screen.exitonclick()
