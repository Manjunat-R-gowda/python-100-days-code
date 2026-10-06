#compare a function down the hogher and lower number game
from text import data
from text import data
from art import logo
from art import vs
import random


def gameing():
    game=True
    current_score=0
    while game:
        compare_1=random.choice(data)
        print(logo)

        print(f"compare A :{compare_1["name"]}, {compare_1["description"]}, {compare_1["country"]}" )
        number=compare_1["followers"]








        print(vs)
        compare_2=random.choice(data)
        print(f"compare B : {compare_2["name"]}, {compare_2["description"]}, {compare_2["country"]} ")
        number_2=compare_2["followers"]




    #who has highest follower a or b type using function and if else block

    
        
        answer_correction=(input("Who has more followers? Type 'A' or 'B': "))
        
        if answer_correction=='a' or answer_correction=='b' and number>number_2 :
            
            current_score=current_score+1

            print(f"You're right! Current score: {current_score}.")
        else:
            print(f"Sorry, that's wrong. Final score:{current_score} ")
            break
    




gameing()
#wrong choice game stop 0 score create a function

#game correct function you are right and score update to 1 and game continue as it is same untill than game false 