# 4. Add a static method in problem 2, to greet the user with hello.


#Line 8 to 10, and line 24.

class Calculator:

    @staticmethod
    def greet():
        print("Hello, User!")

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def sqroot(self):
        print(f"The square root is {self.n**(1/2)}")   #self.n**1/2 implies raise to power 1/2

Calculator.greet()

n = int(input("Enter the number: "))
a = Calculator(n)
a.square()
a.cube()
a.sqroot()

#staticmethod decorator is used when there is no need of object or instance attribute(No need of "self").