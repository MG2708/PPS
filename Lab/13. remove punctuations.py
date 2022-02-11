#remove punctuations
#Date: 22/12/2021

punc = [ '.', ",", "?", "!", "-", "_", ' \ ', "|", ";", ":", " ' ", "( " , ")" , "...", "/"]
m = input("Enter String: ")
print()
n = ""
for i in m:
    if i not in punc:
        n += i
print("Entered String is: \n", m)
print()
print("String after Punctuation Filter is: \n", n)

         
