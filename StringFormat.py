n1 = 10
n2 = 20
name = "maria"
id = 106
print(f"My name is {name} and my id is {id}")
print(f"Calculation by formatting: {n1+n2:.2f}\n")


# single line comment
print("Hello world")
print(420)
''' multi line 
comment'''
name = "maria"
id1 = 106
id2 = 364.0
print(name, id1, id2, "\n")


# upper & lower case
s = "Hello World"
print(s.upper())
print(s.lower())

# remove space at begining
m = " Maria"
print(m)
print(m.strip())
print("After replacing:", m.replace("M", "N"), "\n")


# string slicing
name = "Maria"
slicing = name[0:3]  # start from 0 till 3 [excluding 3]
print(slicing)
print(name[-4:-1])  # same as [1:4]
print(name[:4])
print(name[1:])  # same as [1:5]

# string slicing with skip value
a = "0123456789"
print(a[1:8])
print(a[1:8:2], "\n")


# String function
name = "zannatul"
print(len(name))
print(name.endswith("tul"))
print(name.capitalize())
