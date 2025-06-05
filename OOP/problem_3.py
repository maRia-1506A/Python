'''Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
Does this change the class attribute?'''


class demo:
    a = 4  # class attribute


o = demo()
print(o.a)  # prints class attribute cz instance attribute is not present
o.a = 0  # instance attribute is set
print(o.a)  # prints instance attribute cz instance attribute is present
print(demo.a)  # prints class attribute
