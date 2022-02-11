#Functions
#13/12/2021

def profile(name, surname, pincode):
    print(f' My name is {name} {surname} and the pincode of the city I live is {pincode} !')

def edu(gradu, pg, phd):
    print(f' Graduation: {gradu}, Post Graduation: {pg} and PhD: {phd}')

def age(a):
    print(f' Age (in years): {a}')

name = input("Enter Name: ")
surname = input("Enter Surname: ")
pincode = int(input("Enter Pincode: "))
gradu = input("Enter Graduation Degree: ")
pg = input("Enter Post Graduation Degree: ")
phd = input("Enter PhD Details: ")
a = int(input("Enter Age in years: "))

profile(name, surname, pincode)
age(a)
edu(gradu, pg, phd)
