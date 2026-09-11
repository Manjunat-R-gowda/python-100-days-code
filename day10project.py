import random

from day10 import logo

def add(first_num,second_number):
        return (first_num+second_number)
def sub(first_num,second_number):
         return first_num-second_number
def mul(first_num,second_number):
        return first_num*second_number
def divi(first_num,second_number):
        return first_num/second_number


def calculate():
    print(logo)
    run=True
    first_num=(float(input("what is the first number?:")))
    while run:
        

        print("+")
        print("-")
        print("*")
        print("/")
        pick=(input("pick an operation :"))

        second_number=float(input("what is next number :"))
        dic={"+":add,
            "-":sub,
            "*":mul,
            "/":divi,}
        answer=dic[pick](first_num,second_number)

        print(f"{first_num}{pick}{second_number} =",answer)
        choice=(input(f"Type 'y' to continue calculating with{answer}, or Type 'n' start new calculation:"))
        if choice=="y":
            first_num=answer

        else:
            run=False
            print("\n"*20)
            calculate()  

calculate()



