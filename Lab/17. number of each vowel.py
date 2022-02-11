#Number of each vowel
#Date : 29/12/2021

n = input("Enter a String: ")
ca, ce, ci, co, cu, tc = 0, 0, 0, 0, 0, 0

for i in n:
    if i.lower() == 'a' :
        ca += 1
        tc += 1
    elif i.lower() == 'e' :
        ce += 1
        tc += 1
    elif i.lower() == 'i' :
        ci += 1
        tc += 1
    elif i.lower() == 'o' :
        co += 1
        tc += 1
    elif i.lower() == 'u' :
        cu += 1
        tc += 1
print(f'Number of Vowels in the entered string "{n}" are as follows:')
print("Vowel Count for 'a' or 'A' = ", ca)
print("Vowel Count for 'e' or 'E' = ", ce)
print("Vowel Count for 'i' or 'I' = ", ci)
print("Vowel Count for 'o' or 'O' = ", co)
print("Vowel Count for 'u' or 'U' = ", cu)
print()
print("Total Vowel Count = ", tc) 
        
