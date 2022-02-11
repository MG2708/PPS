#Fibonacci Series
# Module to import
#PPSL ESE PRACTICAL
#DATE : 05/01/2022

#using recursive function

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
