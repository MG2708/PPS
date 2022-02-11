#sum of all digits of a given number
#date : 29/12/2021
m=int(input("Enter a number : "))
m=abs(m)
s=0
while m!=0:
    g=m%10
    s+=g
    m=int(m/10)
ans=int(s)
print("The sum of the digits of given number is : ",ans)
