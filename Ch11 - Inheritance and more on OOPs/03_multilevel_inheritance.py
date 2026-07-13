#       /-> Derived1
# Base-
#       \-> Derived2

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3


p = Employee()
print(p.a)  #Prints attribute a.
# print(p.b)  #Shows error since there is no attribute b in Employee class.


q = Programmer()
print(q.a)  #Prints attribute a, inherited from Emplyee class.
print(q.b)  #Prints attribute b.
# print(q.c)  #Shows error since there is no attribute c in Programmer class.


r = Manager()
print(r.a)  #Prints attribute a, inherited from Programmer class, inherited from Employee class
print(r.b)  #Prints attribute b, inherited from Programmer class.
print(r.c)  #Prints attribute c.