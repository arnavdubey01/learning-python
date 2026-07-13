# Create a class 'Pets' from a class 'Animals' and further create a class 'Dog from 'Pets'. Add a method bark to class 'Dog'.

#It is a good practice to keep the name of class singular(Animal instead of Animals). 
# But here, we will do as problem says.

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")

d = Dog()

d.bark()