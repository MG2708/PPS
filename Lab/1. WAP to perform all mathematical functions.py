#if - else condition to perform simple arithmetic functions for entered two values
#Date 17/11/2021
a=eval(input("Enter a number: "))
b=eval(input("Enter second number with which to perform the simple arithmetic operation: "))
c=input("Choose an operator [ + , - , / , *, % [To get remainder when a is divided by b ] ")
if c == '+' :
    print("The addition of two entered numbers is : " , a+b)
elif c=='-' :
     print("The subtraction of two entered numbers is : " , a-b)
elif c == '*' :
    print("The multiplication of two entered numbers is : " , a*b)
elif c=='/' :
     print("The division of two entered numbers is : " , a / b)
elif c=='%' :
    print("The remainder when a is divided by b is:" , a%b)
else:
    print("Entered Operator is INVALID !!!")
    
     
    
