class parentInfo:
    # constructor (init ase mane constructor)
    def __init__(self, name, number):  # dunder method which is automatically called
        self.name = name
        self.number = number
        print(f"My name is {name} and my number is {number}")


# method
'''def myFamily(self, name, age):
        print(f"My name is {name} and my age is {age}")'''

p1 = parentInfo("Maria", "01608233419")  # object
