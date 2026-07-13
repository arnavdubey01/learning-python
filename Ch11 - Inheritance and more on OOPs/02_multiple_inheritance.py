# Base1 -\
#         -> Derived
# Base2 -/

class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name of the Employee is {self.name} and company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Your language is {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good in {self.language} language")

a = Employee()
b = Coder()
c = Programmer()

c.show()
c.printLanguage()
c.showLanguage()