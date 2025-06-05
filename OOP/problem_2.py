# Write a class “Calculator” capable of finding square, cube and square root of a number
import math


class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n*self.n

    def cube(self):
        return self.n*self.n*self.n

    def square_root(self):
        return math.sqrt(self.n)


calc = Calculator(4)
print(f"The square of 4 is {calc.square()}")
print(f"The cube of 4 is {calc.cube()}")
print(f"The squareRoot of 4 is {calc.square_root()}")
