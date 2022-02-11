#Fibonacci Series by importing module
#PPSL ESE PRACTICAL
#DATE : 05/01/2022

import fibonacci_module

n = int(input("Enter number of terms to be printed: "))
if n <= 0 :
    print("Please input a positive integer only ! ")
else:
    print(f'Printing Fibonacci Series with {n} terms:')
    for i in range(n):
        print(fibonacci_module.fibonacci(i))
        
