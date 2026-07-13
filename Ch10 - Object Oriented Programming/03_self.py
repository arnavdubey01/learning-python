class Employee:
    language = "Python" #This is class attribute
    salary = 1200000

    def getInfo(self):  # "(self)" is important, or else it will show error 
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod   #Since object is not required in 'greet', we add '@staticmethod'. It is a decorator
    def greet():
        print("Good mornimg")
        
#note that "self" is just a convention, it feels more descriptive, any other would also work (self is just a parameter). 

harry = Employee()
harry.language = "JavaScript"   #This is instance attribute

harry.getInfo()
Employee.getInfo(harry) #harry.getInfo() is same as Employee.getInfo(harry), if we don't type getInfo(self) and just type getInfo() after def, it shows error as it lacks paramenter, and in Employee.getInfo(harry), we give parameter "harry". That's why we type 'self'.

harry.greet() #Same a Employee.greet(harry)

#In line 8, if we had not typed @staticmethod, then in line 8, it would have been def greet(self) instead of def greet(). 