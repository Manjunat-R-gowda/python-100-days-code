import random
from art import logo

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1to 100")
print(logo)




def guessnumber():
    choose=input("choose the difficulty Type 'easy' or 'hard' :-")
    number=random.randint(1,100)
    if choose=='easy':
        attempt=11
        while attempt>=1:
            attempt-=1
            print(f"You have {attempt} attempts remaining to guess the number")
            guess=int(input("Make a guess : "))
            if guess<number:
                print("Too Low")
                print("guess again ")
            elif guess>number:
                print("Too High")
                print("guess again")
            elif guess==number:
                print(f"guess the correct number  {number} ")
                break
            else:
                print("you loose try again once")
                break
    if choose=='hard':
        attempt=6
        while attempt>=1:
            attempt-=1
            print(f"You have {attempt} attempts remaining to guess the number")
            guess=int(input("Make a guess : "))
            if guess<number:
                print("Too Low")
                print("guess again ")
            elif guess>number:
                print("Too High")
                print("guess again")
            elif guess==number:
                print(f"guess the correct number  {number} ")
                break
            else:
                print("you loose try again once")
                break

            


guessnumber()

       


    
    

    