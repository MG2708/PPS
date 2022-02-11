#Check if leap year or not
# Date 17/11/21

year = int(input("Please Enter the Year Number you wish to check: "))

if (year%4 == 0) or (year%100 == 0) and (year%400 == 0):
    print(f' Entered year {year} is a Leap Year')
else:
    print(f' Entered year {year} is not a Leap Year')
