#  1. Create a class “Programmer” for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"   #Class attribute, since every programmer is working at microsoft (common attriubte)
    def __init__(self, name, salary, pin):
            self.name = name
            self.salary = salary
            self.pin = pin

p = Programmer("Harry", 1200000, 245001)
print(p.name, p.salary, p.company)

r = Programmer("Rohan", 1000000, 245101)
print(r.name, r.salary, r.company)
