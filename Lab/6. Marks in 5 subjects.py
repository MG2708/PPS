# Grade based on marks in 5 subjects
# Date : 24/11/2021
import sys

s1= float(input("Enter Marks Scored in Mathematics: "))
s2= float(input("Enter Marks Scored in Science: "))
s3= float(input("Enter Marks Scored in English: "))
s4= float(input("Enter Marks Scored in Hindi: "))
s5= float(input("Enter Marks Scored in Social Science: "))
print()
avg= (s1 + s2 + s3 + s4 + s5)/5
print("Scored Percentage:", avg)
if avg >= 90 :
    print(" Outstanding : Grade A* ")
elif avg>= 75 and avg <=89:
    print(" Excellent : Grade A ")
elif avg>= 56 and avg <=74:
    print(" Very Good : Grade B ")
elif avg>= 35 and avg <=55:
    print(" Good : Grade C ")
elif avg <35:
    print(" Scope for Improvement : Grade D ")
else:
    sys.exit("Invalid Input, Recheck !")


