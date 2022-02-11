#Inverted Star Pattern
# Date : 01/12/2021
n=int(input("Enter number of rows of the pattern: "))
print()
print("Printing Star Pattern:")
print()
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
print()
print("Printing Inverted Star Pattern:")
print()
for j in range(n,0,-1):
    print(' '*(n-j)+'* '*(j))

"""
n=int(input("Enter number of rows: "))
for i in range(0,n+1):
    print("* " * i)
print()
for j in range(n,0,-1):
    print("* " * j)
"""
