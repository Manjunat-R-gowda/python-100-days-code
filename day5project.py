import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
numbers=['1','2','3','4','5','6','7','8','9','10']
symbols=['#','@','$',"%",'^','()','_']

print("welcome to the py generator")
nr_letters=int(input("How many letters in password"))
nr_numbers=int(input("How many numbers in password"))
nr_symbols=int(input("how many symbols in password"))


#easy level
password=' '

for char in range(0,nr_letters):
    password+=random.choice(letters)


for char in range(0,nr_numbers):
    password+=random.choice(numbers)


for char in range(0,nr_symbols):
    password+=random.choice(symbols)


print(password)




#hard level
password_lis=[ ]
for char in range (0,nr_letters):
    password_lis.append(random.choice(letters))

for char in range (0,nr_numbers):
    password_lis.append(random.choice(numbers))

for char in range(0,nr_symbols):
    password_lis.append(random.choice(symbols))

print(password_lis)
random.shuffle(password_lis)
print(password_lis)

password=' '
for char in password_lis:
    password+=char
print(f"your password is:- ",password)