'''Write a class vector representing a vector of n dimensions. Overload the + and *
operator which calculates the sum and the dot(.) product of them.'''


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # return as string type that why use return vector(.....)
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # return normal plain number
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)

print(f"v1 + v2 :{v1+v2}")
print(f"v1 * v3: {v1*v2}")

print(f"v1 + v2 :{v1+v3}")
print(f"v1 * v3: {v1*v3}")
