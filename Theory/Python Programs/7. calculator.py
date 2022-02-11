# function
#calculator
# 13/12/2021
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b
    
a=eval(input("Enter Number 1: " ))
b=eval(input("Enter Number 2: " ))
print("The sum of entered two numbers:", a,"and", b, "is:", add(a,b))
print("The subtraction of entered two numbers:", a,"and", b, "is:", sub(a,b))
print("The product of entered two numbers:", a,"and", b, "is:", multi(a,b))
print("The division of entered two numbers:", a,"and", b, "is:", div(a,b))
