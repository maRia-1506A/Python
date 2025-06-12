# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, sub):
        return Complex(self.r + sub.r, self.i + sub.i)


