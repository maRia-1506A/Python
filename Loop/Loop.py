i = 0
while i < 10:
    print("While loop")
    i += 1

'''
for loop:
either a list, a tuple, a dictionary, a set, or a string
'''

fruits = ["apple", "watermelon", "banana", "cherry"]
for x in fruits:
    if (x == "banana"):
        break
    print(x, "\n")


# range func
for i in range(1, 6):
    print(i)
print('')


# for loop with else
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done\n")  # this is printed when the loop exhausts!


# pass statement
l = [1, 7, 8]
for item in l:
    pass
