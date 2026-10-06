from prettytable import PrettyTable
from typing import Any
from termcolor import colored

print("winter arc day1 ...")

def _colored(field: str, val: Any) -> str:
    if isinstance(val, (int, float)):
        if val >= 0:
            return colored(f"{val:.2f}", "green")
        return colored(f"{val:.2f}", "red")
    elif isinstance(val, str):
        return colored(val, "blue")
    return f"{val}"

table = PrettyTable(("city", "population"))
table.custom_format = _colored

for row in [["hassan", 5000], ["mandya", 20000]]:
    table.add_row([row[0], row[1]])
print(table)


from turtle import Turtle
import turtle
# Set up the screen
wn = turtle.Screen()
wn.title("winter arc day 2 ")
wn.bgcolor("green")
# Create a turtle named "t"
t = turtle.Turtle()
t.color("yellow")
t.pensize(30)
t.speed(1)  # Set drawing speed
# Draw a square
for _ in range(7):
    t.forward(100)  # Move forward 100 pixels
    t.right(90)
    t.circle(3)
    t.begin_fill()    # Turn right 90 degrees
# Finish the program
turtle.done()
