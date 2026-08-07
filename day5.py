for i in range(1,11):
    print(i)


for i in range(1,21):
    if i%2==0:
        print(i)

sum=0
for i in range(1,101):
    sum+=i
print(sum)

for m in "manjunath gowda":
    print(m)

for i in range(1,10):
    print(f"1*{i}=",i)

for i in range (1,10):
    for j in range(1,10):
        print(f"{i}*{j}=",i*j)

string=input("enter your string:-")
vowels="a,e,i,o,u,A,E,I,O,U"
count=0
for vn in string:
    if vn in vowels:
        count+=1

print(count)


