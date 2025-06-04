class NewClass1():  # class
    language = "py"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


a = NewClass1()  # object / instance
a.language = "JS"
print(a.language, a.salary)
a.getInfo()  # NewClass1.getInfo() [both are same]
