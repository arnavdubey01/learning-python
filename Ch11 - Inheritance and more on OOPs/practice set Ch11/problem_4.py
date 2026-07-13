# 4. Write a class ‘Complexʼ to represent complex numbers, along with 
# overloaded operators ‘+ʼ and ‘*ʼ which adds and multiplies them


class Complex:
    def __init__(self, a, b):  # a is real part and b is imaginary part   
        self.a = a
        self.b = b 

    def __add__(self, c2):
        return Complex(self.a + c2.a, self.b + c2.b)
    
# (a+ib)*(p+iq)=ap+iqa+ibp-bq= ap - bq + i(qa+bp) 
    def __mul__(self, c2):
        return Complex(self.a*c2.a - self.b*c2.b, c2.b*self.a + self.b*c2.a)
    
    def __str__(self):
        return (f"{self.a} + {self.b}i")
        
        
c1 = Complex(1,2)
c2 = Complex(3,5)

print(c1 + c2)
print(c1*c2)
 