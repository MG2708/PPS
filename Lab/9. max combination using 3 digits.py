# Input 3 digits, print max possible combination
# Date: 01/12/2021

import sys

a = int(input("Enter First Digit : "))
b = int(input("Enter Second Digit : "))
c = int(input("Enter Third Digit : "))
if a > 9 or b > 9 or c > 9:
    sys.exit("Invalid Input, Enter only Single Digits, Recheck !")
    
m=[a,b,c]
n=[]
print()
print("Printing all possible unique combinations using entered digits:", a,b,c)
print()
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i != j  and j != k and k != i):
                x= [m[i] , m[j] , m[k]]
                if x not in n:  # to find unique combinations
                    n.append(x)
d=len(n)
for i in range(0,d):
    print(*n[i]) 
              
print()
print("Printed Number of Unique Combinations: ",d)
