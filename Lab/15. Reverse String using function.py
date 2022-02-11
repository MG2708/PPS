#Reverse string
#Functions
#Date : 29/12/2021

def rev(x):
    temp=" "
    for i in x:
        temp=i+temp
    return temp
    
n=input("Enter a string: ")

print('Entered String:', n)
print("Reversed String:", rev(n))

"""
def reverse(x):
    s = x[ : : -1]
    print(s)
reverse(n)
"""
    
