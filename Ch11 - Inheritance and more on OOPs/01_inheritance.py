class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of the programmer is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")

# To do the same as above, we can use inheritance instead of copy pasting Employee class.

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)

#This is more efficient than copying and pasting a class again and again.
#Here, 'Employee' is base/parent class 
#'Programmer' is called derived class

a.name = "Rohan"
a.salary = 500000

b.name = "Shyam"
b.salary = 800000
b.language = "Python"

a.show()          # Calls Employee.show()
b.show()          # Inherited from Employee
b.showLanguage()  # Programmer method

#Inheritance is basically creating a new class from as existing class.