Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''



import random


choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

l = ["Rock", "Paper", "Scissors"]


choice = l[choice]
computer_choice = random.choice(l)

print(computer_choice)


if choice == computer_choice:
    print("Tie! Please try again.")

elif choice == "Rock":
    if computer_choice == "Scissors":
        print("You won! Rock wins.")
    else:
        print("You lose!")

elif choice == "Paper":
    if computer_choice == "Rock":
        print("You won! Paper wins.")
    else:
        print("You lose!")

elif choice == "Scissors":
    if computer_choice == "Paper":
        print("You won! Scissors win.")
    else:
        print("You lose!")