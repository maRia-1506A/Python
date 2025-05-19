class allMethod:
    # isinstance method
    def instanceMethod(self):
        print("This is Instance Method")

    # class method
    @classmethod
    def classMethod(cls):
        print("This is class Method")

    # static method
    @staticmethod
    def staticMethod():
        print("This is Static Method")


obj = allMethod()
obj.instanceMethod()

allMethod.classMethod()  # calling by class name
obj.classMethod()  # calling by obj

allMethod.staticMethod()
obj.staticMethod()
