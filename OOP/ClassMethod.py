class Employee:
    a = 1

    # class method is used to show the class attribute
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45
e.show()
