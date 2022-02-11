#Class - Sales System for Cars
#Date 28/12/2021
class Car():
        company = " "
        produced_no = 0
        sold_no = 0

        def sales(self):
                if self.sold_no == self.produced_no:
                        print(f'Sales of {self.sold_no} out of {self.produced_no} manufactured cars by {self.company}. The company is performing well.')
                else:
                        print(f'Sales of {self.sold_no} out of {self.produced_no} manufactured cars are not enough. Sales should be improved by {self.company}')

tata = Car()
tata.company = "TATA"
tata.produced_no = 500
tata.sold_no = 400
tata.sales()
print()

mahindra = Car()
mahindra.company = "MAHINDRA"
mahindra.produced_no = 500
mahindra.sold_no = 500
mahindra.sales()
print()

honda = Car()
honda.company = "HONDA"
honda.produced_no = 500
honda.sold_no = 500
honda.sales()
print()

kia = Car()
kia.company = "KIA"
kia.produced_no = 400
kia.sold_no = 400
kia.sales()
print()

toyota = Car()
toyota.company = "TOYOTA"
toyota.produced_no = 400
toyota.sold_no = 350
toyota.sales()
print()




