# int data type
int = 1234
print(int, "is the integer value")

# string data type
string = "Name is a string"
print(string)

# String concatenation
name1 = "Zannatul"
name2 = "Farzana"
print(name1+name2)
print("My name is"+" "+name2)

# compare
x = 10
y = 5
print(x == y)
print(x > y)

# binary type(bytes) [range is 0-256]
list1 = [1, 2, 200, 100]
b1 = bytes(list1)
# bytes value cannot be changed(like b[0]=10)= immutable
print(list1)


# binary type(byte array) [range is 0-256]
list2 = [1, 2, 200, 100]
b2 = bytearray(list2)
b2[1] = 10
print(b2[1])

# none type (define NULL value)
x = None
print(type(x))

# list type data
l1 = ["maria", "afridi", "efath", "sumaiya"]  # mutable(can change)
l1[2] = "aziz"
print(l1)

# tuple type data
t1 = (5, 10, 15, 20)  # immutable
print(t1)

# range type data
ran = range(6)
for i in ran:
    print(i)

# Check data type
com = 123j
print("com is", type(com))

checkBool = False
print("checkBool", type(checkBool))

print("b1", type(b1))
print("b2", type(b2))
print("l1 is", type(l1))
print("t1 is", type(t1))
