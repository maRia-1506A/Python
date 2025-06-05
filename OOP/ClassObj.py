class NewClass1():  # class
    name = ''  # class attribute
    number = ''
    id = ''
    section = ''
    language = "py"
    salary = 120000


a = NewClass1()  # object / instance
b = NewClass1()  # object
a.name = 'maria'
a.id = 106

b.name = 'afridi'
b.number = '01608233419'

print(a.name, a.id, a.language, a.salary)
print(b.name, b.number, b.language, b.salary)
