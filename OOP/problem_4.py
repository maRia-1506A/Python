# Add a static method in problem 2, to greet the user with hello.
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

    @staticmethod
    def hello():
        print("Hello User!")


calc = Calculator(4)
calc.hello()
print(f"The square of 4 is {calc.square()}")
print(f"The cube of 4 is {calc.cube()}")
print(f"The squareRoot of 4 is {calc.square_root()}")
