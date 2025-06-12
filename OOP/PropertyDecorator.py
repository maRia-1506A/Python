class Employee:
    a = 1

    # class method is used to show the class attribute
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property  # getter method
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Zannatul Maria"
print(e.name)
print(e.fname)
e.show()
