class Employee:
    language = "Python" #Class attribute
    salary = 1200000

    def __init__(self, name, salary, language): #After self, we have added three values here, now we have to pass those three values when calling (Line 11).
        self.name = name
        self.salary = salary
        self.language = language    # Be careful with typos. 
        print("I am creating an object")

harry = Employee("Harry", 1300000, "JavaScript")  #dunder method is called.

print(harry.name, harry.salary, harry.language)