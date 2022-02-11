#Fibonacci Series 
# Date 24/11/2021

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

n = int(input("Enter number of terms: "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Printing Fibonacci Series:")
   for i in range(n):
       print(fibo(i))
