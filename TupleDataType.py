newList = (1, 2, 3, "maria", True, 'm')
print(type(newList))
print(newList[2])

# neg index
print(newList[-3])

# range of index
print(newList[3:6])
print('')


# update tuple
tuple1 = ("m", "r", "i")
print(tuple1)

a = list(tuple1)
a.append("a")
a.insert(1, "a")
tuple1 = tuple(a)
print(tuple1)
print('')


# unpack tuple
tuple2 = ("apple", "banana", "cherry", "dog", "elephant")
(a, b, c, d, e) = tuple2
print(d)

# asterisk using
(a1, *a3, a2) = tuple2
print(a3)
print('')


# loop tuple
tuple3 = [10, 20, 30, 40, 50]

# for loop
for x in tuple3:
    print(x)

# using range & len
print("Index Number:")
for y in range(len(tuple3)):
    print(y)

print("Value:")
for z in range(len(tuple3)):
    print(tuple3[z])

# while loop
tuple4 = ['a', 's', 'd', 'f', 'g']
print("While loop:")
i = 0
while i < len(tuple4):
    print(tuple4[i])
    i += 1
print('')


# join tuple
t1 = [1, 2, 3, 4, 5]
t2 = [6, 7, 8, 9, 10]
t3 = t1 + t2
print(t3)

# multiply tuple
t4 = t1*2
print(t4)
print('')


# method tuple
mt = [1, 2, 2, 2, 5, 6, 9, 87, 3, 5, 6, 4]
ind = mt.index(5)  # index method
print("Index of 5:", ind)

cnt = mt.count(2)  # count method
print("Counting 2:", cnt)
