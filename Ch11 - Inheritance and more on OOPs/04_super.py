class Employee:
    def __init__(self):
        print("Constreuctor of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Contructor of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) # Constructor of Employee is printed

o = Programmer()
print(o.a, o.b) # Constructor of Programmer is printed

o = Manager()
print(o.a, o.b, o.c) # Constructor of Manager is printed

# What if we want to print Constructor of Programmer with the constructor of Manager?
# (We want Base constructor to be printed when printing derived constructor. :

# We use super().__init__()

#SEE(Line 42):

class Employee:
    def __init__(self):
        print("Constreuctor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Contructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Manager()
print(o.a, o.b, o.c) # Constructor of Manager is printed along with Base class constructor