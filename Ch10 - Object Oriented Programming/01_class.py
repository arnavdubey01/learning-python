# A class is a blueprint for creating object:

class Employee:
    language = "python" #This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"    #This is object/instance attribute
print(harry.name, harry.language)

rohan = Employee()
rohan.name = "Rohan Robinson" #This is object/instance attribute
print(rohan.name, rohan.salary, rohan.language) 

#Think of class as an empty form, object "fills" the form.
#Here, name is object attribute and salary and language are class attributes as they
# directly belong to the class.