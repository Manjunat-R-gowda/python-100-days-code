a=int(input("enter your a number;-"))
if a<0:
    print("The number is negative")
else:
    print("The number is postive")

if a%2==0:
    print("the number is even")
else:
    print("the number is odd")

a=10
b=20
if a>b:
    print("a is greetar")
else:
    print("b is greater")

leap=int(input("enter your leap year;-"))
if (leap%4==0 and leap%100!=0 and leap%400==0):
    print("leap year is ",leap)
else:
    print("this is not a leap year")

marks=int(input("enter your marks;-"))
if marks>=35: print("pass")
else:
    print("fail")

age=18
valid_id=True
print("is eligible ") if age>=18 and valid_id else("not eligible")

num=int(input("enter your number;-"))
if num/3 and num/5:
    print("divisible is possible")
else:
    print("not possible")

v=input("enter your string;-")
count=0
vowels='a,e,i,o,u,A,E,I,O,U'
if  'voweles' in v:
    count+=1
    print("the number of voweles")

else:
    print(" the conosonats is,count",count)

num=int(input("enter your number;-"))
if num>=1 and num<=100:
    print("the number is 1 to 100")

else:
    print("the number is not to 1to 100")

