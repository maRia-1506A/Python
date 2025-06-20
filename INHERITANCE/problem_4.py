# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, com):
        return Complex(self.r + com.r, self.i + com.i)

    def __mul__(self, com):
        real = self.r * com.r - self.i * com.i
        imag = self.r * com.i + self.i * com.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)
