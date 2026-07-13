# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector

#Line 11, 24, 25, 30

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
    
    def __len__(self):
        return 3
    
v1 = Vector(1,3,5)
v2 = Vector(4,6,3)

print(f"Length of vector is: {len(v1)}")