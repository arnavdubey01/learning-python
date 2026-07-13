#5. Write a class vector representing a vector of n dimensions. Overload the
#+ and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        result = Vector(self.a + other.a, self.b + other.b, self.c + other.c )
        return result

    def __mul__(self, other):
        result = self.a*other.a + self.b*other.b + self.c*other.c
        return result

    def __str__(self):
        return (f"Vector({self.a}, {self.b}, {self.c})")
    
v1 = Vector(1,3,5)
v2 = Vector(4,6,3)

print(v1 + v2)
print(v1*v2)

v3 = Vector(1,1,1)
print(v1+v3)
print(v1*v3)