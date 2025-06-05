# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id


prg1 = Programmer("Maria", 1200000, 240106)
print(f"This is {prg1.name} who is working at {prg1.company}\nId is {prg1.id}\nSalary is {prg1.salary}\n")
prg2 = Programmer("Faisal", 1200000, 240107)
print(f"This is {prg2.name} who is working at {prg2.company}\nId is {prg2.id}\nSalary is {prg2.salary}")
