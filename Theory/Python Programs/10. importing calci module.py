#Importing module
#17/12/2021

import calculator as calci

a=eval(input("Enter a number: "))
b=eval(input("Enter second number with which to perform the simple arithmetic operation: "))
c=input("Choose an operator [ + , - , / , * ] ")
if c == '+' :
    print("The addition of two entered numbers is : " , calci.add(a,b))
elif c=='-' :
     print("The subtraction of two entered numbers is : " , calci.sub(a,b))
elif c == '*' :
    print("The multiplication of two entered numbers is : " , calci.multi(a,b))
elif c=='/' :
     print("The division of two entered numbers is : " , calci.div(a,b))
else:
    print("Entered Operator is INVALID !!!")
    
