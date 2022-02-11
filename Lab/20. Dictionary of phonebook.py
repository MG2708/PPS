#Dictionary : Phonebook
#Date: 03/01/22

phonebook = { }
phonebook['Mohan'] = 9978445512
phonebook['Mahesh'] = 9765432980
phonebook['Suresh'] = 9955643218
phonebook['Ayush'] = 6353634318
phonebook['Jasprit'] =8769120542
print(phonebook)
print()

#initialise
pb = {"Mohan" : 9978445512, "Mahesh" : 9765432980, "Suresh" : 9955643218, "Ayush" : 6353634318, "Jasprit" : 8769120542}
print("Initialised Dictionary Phonebook:")
print(pb)
print()

#adding elements
pb['Ramesh'] = 9875436671
pb.update(Samir = 7698634518)
print("Updated Dictionary after adding elements is:")
print(pb)
print()

#removing elements
del pb['Mohan']
pb.pop('Suresh')
print("Updated Dictionary after removing elements is:")
print(pb)
