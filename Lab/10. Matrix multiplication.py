#Matrix Multiplication
#Date : 08/12/2021
import sys

print("Please input two matrices of order m X n and n X p ")
print()

print("For Matrix 1:")
m=int(input("Enter number of rows: "))
n=int(input("Enter number of column: "))
A = [ ]
print("Entries to be entered row - wise")
for i in range(m):
    a=[ ]
    for j in range(n):
        a.append(int(input("Enter Element: ")))
    A.append(a)
print()

print("For Matrix 2:")
p=int(input("Enter number of rows: "))
q=int(input("Enter number of columns: "))
B = [ ]
print("Entries to be entered row - wise")
for i in range(p):
    b=[ ]
    for j in range(q):
        b.append(int(input("Enter Element: ")))
    B.append(b)
print()

print("Printing Entered Matrices:")
for r in A:
    print(r)
print()
for r in B:
    print(r)
print()

if n != p:
    print("As per fundamentals of Matrix Multiplication, number of columns of first matrix should be equal to number of rows of second matrix ... ")
    sys.exit("Hence, Matrices entered not applicable for multiplication!")
    
rows,column=m,q
result = [([0]*column) for i in range(rows)]

print("Performing Matrix Multiplication !")
for i in range(m):  #rows of A
    for j in range(q):  #columns of B
        for k in range(p):  #rows of B
            result[i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)
            


    

