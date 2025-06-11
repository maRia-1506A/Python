class Employee:
    company = "Microsfot"

    def show(self):
        print(
            f"The name of the employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     comapny = "Nest IT"

#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(
#             f"The name is {self.name} and he is good with {self.langiage} language")

class Programmer(Employee):  # inheritate class
    comapny = "Nest IT"

    def showLanguage(self):
        print(
            f"The name is {self.name} and he is good with {self.langiage} language")


emp = Employee()
prg = Programmer()
print(emp.company, prg.comapny)
