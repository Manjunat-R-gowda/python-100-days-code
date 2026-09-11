def calc(a,b):
    print("calculator")
    print(a+b)
    print(a-b)
    print(a*b)
calc(2,5)

def pos(num):
    if num<0:
        print("THe number is negative",num)
    elif num==0:
        print("The number is 0",num)
    else:
        print("The number is positive",num)

pos(6)
pos(-69)
pos(0)

def person(name):
    print("heloo",name)

person("manjunath")
person(name="rakshi")

def square(num):
    print(num*num)

square(2)
square(510)

def eve(num):
    if num%2==0:
        print("even number")
    else:
        print("odd number")
eve(20)

def maximun(a,b):
    if a>b:
        print("the number is large ",a)
    else:
        print("the number is large",b)

maximun(20,52)

def area(length,width):
    a=length*width
    print(a)

area(20,50)

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)

factorial(5)

def num(n):
    for i in range(1,n):
        print(i)
num(9)

def summ(n):
    sum=0
    for i in range(0,n+1):
        sum+=i
    print(sum)
summ(5)




def count_vowel(text):
    vowels = 'aeiouAEIOU'
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    print(count)

count_vowel("manju")

def reverse(text):
    text=text[::-1]

    print(text)

reverse("python")

i=0
while i<10:
    i+=1
    print(i)

i=10
while i>1:
   i-=1
   print(i)

i=1
while i<20:
    if i%2==0:
       
        print(i)
    i+=1

print("i am done")


        
