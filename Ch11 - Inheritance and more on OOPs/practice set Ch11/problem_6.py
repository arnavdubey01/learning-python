# 6. Write __str__() method to print the vector as follows:
# xi + yj + zk (eg: 7i + 5j + 8k)

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
        return (f"({self.a}i, {self.b}j, {self.c}k)")
    
v1 = Vector(1,3,5)
v2 = Vector(4,6,3)

print(v1 + v2)
print(v1*v2)

v3 = Vector(1,1,1)
print(v1+v3)
print(v1*v3)