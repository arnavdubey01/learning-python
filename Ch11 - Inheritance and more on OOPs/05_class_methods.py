# A way to access class directly in a method.
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

# Instead of (self), we use (cls)
class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 43

e.show()    #Prints class attribute (1), not the instance attribute(43).
            # Else if classmethod was not used, it would have printed instance attribute.