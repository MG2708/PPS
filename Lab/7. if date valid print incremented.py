#Check if entered date is in valid form
#Print Incremented Date
#Date : 24/11/2021

from datetime import *

idate=input("Enter date in the format dd/mm/yyyy: ")
dd,mm,yyyy=idate.split('/')
dd=int(dd)
mm=int(mm)
yyyy=int(yyyy)
if mm in [1,3,5,7,8,10,12]:
    mv= 31
elif mm in [4,6,9,11]:
    mv= 30
elif (yyyy%4==0 and yyyy%100!=0 or yyyy%400==0):
    mv= 29
else:
    mv= 28

if mm < 1 or mm > 12 or dd < 1 or dd > mv :
    sys.exit("Invalid Date Entered, Recheck !")
elif  dd==mv and mm!=12:
    dd= 1
    mm+= 1
elif dd== 31 and mm == 12:
    dd = 1
    mm = 1
    yyyy +=1
else:
    dd +=1

odate= date(yyyy,mm,dd)
fdate=odate.strftime("%d/%m/%Y")
print("Entered Date:" , idate)
print("Incremented Date: ",fdate)


    
