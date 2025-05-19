class Parent:
    def __init__(self, name, fatherName):
        self.name = name
        self.__fatherName = fatherName  # private/encapsulate
        print(self.__fatherName)  # class er byre run kra jbena


p1 = Parent("Maria", "Kamal")
print(p1.fatherName)
