class Employee:
    language = "Python" #Class attribute
    salary = 1200000

    def __init__(self): #It is a "dunder method" (Starts from double underscores '__'.)
        print("I am creating an object")

harry = Employee()  #dunder method is called.

#Line 5: dunder method. It is automatically called in python.

harry.name = "Harry"
print(harry.name, harry.salary)


rohan = Employee()  #dunder method is called again

#Not all dunder methods are called, but "__init__" is a dunder method which always get called like this. 

# __init__ is a constructor.