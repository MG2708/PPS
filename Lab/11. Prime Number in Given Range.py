#Prime Numbers in given range
# Date: 15/12/2021

l = int(input("Enter Lower Limit of the Range: "))
u = int(input("Enter Upper Limit of the Range: "))
print()
c=0
print(f'Printing Prime Numbers Between Entered Range {l} to {u}')
for num in range(l, u+1):
    if num>1:
        for i in range(2, num):
            if (num%i==0):
                break
        else:
            print(num)
            c+=1
print()
print("Total Prime Numbers Printed = ",c)
                
