'''Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
which changes the value of increment based on the salary.
'''


class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        '''new salary = old salary + old salary * increment / 100
           new salary = old salary (1 + increment / 100)
           increment = ((new salary / old salary) - 1) * 100 '''
        self.increment = ((salary / self.salary) - 1) * 100


emp = Employee()
# Calls the @property method and prints the salary after increment
print(emp.salaryAfterIncrement)

# Calls the @setter and calculates the increment needed to get to 280.8
emp.salaryAfterIncrement = 280.8
print(f"Increment: {emp.increment}")
