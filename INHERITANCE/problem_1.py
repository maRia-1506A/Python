# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvec:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def showDetails(self):
        print(f"The 2d vector is {self.i}i + {self.j}j")


class threeDvec(twoDvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def showDetails(self):
        print(f"The 3d vector is {self.i}i + {self.j}j + {self.k}k")


twod = twoDvec(1, 2)
threed = threeDvec(4, 5, 6)

twod.showDetails()
threed.showDetails()
