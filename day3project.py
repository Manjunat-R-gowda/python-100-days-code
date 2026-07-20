print('''




                     _                 __                 
             __.--**"""**--...__..--**""""*-.            
           .'                                `-.         
         .'                         _           \        
        /                         .'        .    \   _._ 
       :                         :          :`*.  :-'.' ;
       ;    `                    ;          `.) \   /.-' 
       :     `                             ; ' -*   ;    
              :.    \           :       :  :        :    
        ;     ; `.   `.         ;     ` |  '             
        |         `.            `. -*"*\; /        :     
        |    :     /`-.           `.    \/`.'  _    `.   
        :    ;    :    `*-.__.-*""":`.   \ ;  'o` `. /   
              ;   ;                ;  \   ;:       ;:   ,/
         |  | |            [bug]      /`  | ,      `*-*'/ 
         `  : :  :                /  /    | : .    ._.-'  
          \  \ ,  \              :   `.   :  \ \   .'     
           :  *:   ;             :    |`*-'   `*+-*       
           `**-*`""               *---*                 

''')

print("welcome to treasure island your mission is to find the treasure")
treasure=input("enter your left or right:-")
if treasure=='right':
    print("game over !")


if treasure=='left':
    print(" left")

s=input("enter your swim or wait:- ")
if s=='swim':
    print("attacked by trout game over")
if s=='wait':
    print("wait")

    door=input("enter your door red,yellow,green:- ")
    if door=='red':
        print("burned by fire game over")
    elif door=='blue':
        print("eaten by beasts game over")
    elif door=='yellow':
        print("you will win !")
else:
    print("game over! please try again a game")



