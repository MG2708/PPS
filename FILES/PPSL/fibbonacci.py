# -*- coding: utf-8 -*-
"""fibbonacci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12k3W0KQ6l0wz8cDwZS4XjTeTCOz_77rM
"""

#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       result = (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
    
       return result