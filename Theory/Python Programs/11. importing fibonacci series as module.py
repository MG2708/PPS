import recur_fibo

n = int(input("Enter number of terms: "))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Printing Fibonacci Series:")
   for i in range(n):
       print(recur_fibo.fibo(i))
