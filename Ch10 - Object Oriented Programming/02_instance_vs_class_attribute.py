class Employee:
    language = "Python" #This is class attribute
    salary = 1200000

harry = Employee()
harry.language = "JavaScript"   #This is instance attribute
print(harry.salary, harry.language) 

#See how instance attribute is printed, not the class attribute

#NOTE: instance attribute takes preference over class attributes
#      during assignment and retrival.

#So, if we have not typed harry.language = "JavaScript" under harry = Employee(), 
# it would have printed "Python"(Class attribute).