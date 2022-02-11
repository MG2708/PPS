#Fibonacci Series 
# Date 24/11/2021

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

