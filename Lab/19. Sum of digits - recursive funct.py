#sum of all digits of a given number
#recursive function
#date : 29/12/2021

def digitsum(m):
    m = abs(m)
    if m < 10:
        return m
    else:
        return m%10 + digitsum(m//10)
    
m=int(input("Enter a number : "))
ans = digitsum(m)
print("The sum of the digits of given number is : ",ans)
