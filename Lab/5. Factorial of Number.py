#Factorial of Number
# Date 24/11/2021
def fact(n):
   if n==1:
      return n
   else:
      return n * fact(n-1)

n=int(input("Enter Number: "))
if n<0:
   print("Factorial is not defined for Negative Numbers!")
elif n==0:
   print("Factorial = 1")
else:
   print("The factorial is:", fact(n))

