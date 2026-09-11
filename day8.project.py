logo='''
              __________________________
           .-'                          '-.
         .'                                '.
        /                                    \
       |              🔨 AUCTION             |
        \                                    /
         '.                                .'
           '-.__________________________.-'
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                      /  \
                     /____\
                        '''
print(logo)

def highest(bidding):
  highest_bid=0
  max(bidding)
  winner=" "
  for bidder in bidding:
    bid_amount=bidding[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is{winner} and with  bid of ${highest_bid}")


sin=True
di={}
while sin:
  print("welcome to the secreat auction bid " )
  name=input("what is your name :- ")
  price=int(input("what's your bid:-$"))
  
  di[name]=price
  type=input("Are there any other bidders ? Type 'yes' or 'no' ")
  if type=="no":
    sin=False
    highest(di)
  elif type=="yes":
    print("\n"*20)




 
  


