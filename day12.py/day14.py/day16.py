"""from turtle import Turtle , Screen
timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.color("red")
screen=Screen()
screen.exitonclick() """

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("pokoman name",["pikachu","squritle","charamander"])
table.add_column("type",["electric","water","fire"])
table.align="l"
print(table)

