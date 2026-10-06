def water(bill):
    bill=0
    water=input("how many liters consumed water")
    print(water)
    if water<'50':
        print("200 rupees")

    else:
        print("500 rs")






is_money=True   
while is_money:
    print("--------Water rent----------")

    home=int(input("enter the home number :"))
    if home=='1':
        print("home bill and water rent ")
   
    else:
        print("next day i will upadte")
    is_money=False

water(200)
    




    
