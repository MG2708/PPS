#Classes : Complex Number
#Date : 04/01/2022

class cn:
        def __init__(self, r, i):
                self.r = r
                self.i = i

        def print_cn(self):
                if self.i == 0:
                        print(self.r, "+", self.i,"i", end=' ')
                        print('=' , self.r)
                else:
                        print(self.r, "+", self.i,"i", end = ' ')
                        print('=' , self.i,"i")
                
a = int(input("Enter Real Part of the Complex Number: "))
b = int(input("Enter Imaginary Part of the Complex Number: "))
complex_number = cn(a,b)
complex_number.print_cn()

