

import random
game=True
while game:
      project='''

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                              | |           
      '------'
      
'''

      print(project)    

      typing=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
      if typing=="n":
            break
      num=[1,5,6,9,10,4,5,6]
      nums=[]
      p=random.choice(num)
      m=random.choice(num)
      nums.append(p)
      nums.append(m)
      n=p+m
      print(f"your cards {nums}, current score: {n}")

      computer_card=[]
      card_computer=random.choice(num)
      computer_card.append(card_computer)
      print(f"computer first card {computer_card}")
      ty=input("Type 'y' to get another card, type 'n' to pass:")
      if ty=="y":
            new=random.choice(num)
            nums.append(new)

            new_co=n+new
            print(f"your cards {nums}, current score: {new_co}")
            print(f"computer first card {computer_card}")
      
            pri=(f"your final hand:{nums}, final score:{new_co} ")
            print(pri)
            new_one=random.choice(num)
            new_second=random.choice(num)
            computer_card.append(new_one)
            computer_card.append(new_second)
            total=card_computer+new_one+new_second
            final=(f"computer score:{computer_card}, final score:{total} ")
            print(final)
            if new_co>total and new_co<22:
                  if total>new_co and total<22 :
                        print("you win 😃 ")
            elif new_co==total or total==new_co:
                  print("Draw  🙃")
            else:
                  print("you lose 😤")
      
      if ty=="n":
      
            
            final_answer=(f"your final hand:{nums}, final score:{n} ")
            print(final_answer)
            new_one=random.choice(num)
            new_second=random.choice(num)
            computer_card.append(new_one)
            computer_card.append(new_second)
            total=card_computer+new_one+new_second
            manu=(f"computer score:{computer_card}, final score:{total} ")
            print(manu)
            if n>total and n<22:
                  if total>n and total<22:
                        print("you win 😃")
            elif n==total or total==n:
                  print("Draw  🙃")
            else:
                  print("you lose 😤")


      
