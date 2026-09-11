def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

dice={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

print(dice["*"](n1=int(input("what is the first number?:")),n2=int(input("what is the second number?:"))))

