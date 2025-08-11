l1 = [1, 2, 3]
print(l1)
print("Index 1:", l1[1])

l1[2] = 30
print(l1)

l2 = ["zannatul", "farzana", "maria"]
print(l2)

l3 = [True, False, False, True]
print(l3)
print(" ")


# access list items
list1 = ["java", "c", "python", "js"]
print(list1)
print(list1[2])

# change list items
list1[1] = "css"
print(list1)

# add list items
list1.append(10)  # append(at last)
print(list1)

list1.insert(1, "c++")  # insert(at any index)
print(list1)

# remove list items(all method)
newList = ["maria", "faisal", "aziz", "efath", 420, 100.55]
print(newList)

newList.remove("aziz")  # by value
print(newList)

newList.pop(3)  # by index(by default last item delete krbe)
print(newList)

del newList[3]  # by del method
print(newList)

newList.clear()  # clear all items
print(newList)
print(" ")


# loop list
loopList = ["zannatul", "farzana", "maria", "afridi", "tanmoy"]

# for loop
for i in loopList:
    print(i)

# index through range and len
for j in range(len(loopList)):
    print(j)

# while loop
x = 0  # intial index
while x < len(loopList):
    print(loopList[x])
    x = x+1
print("")


# list comprehension
list1 = [1, 2, 3, 4, 5]
result = [k*k for k in list1]
print(result)

result2 = [l+10 for l in list1]
print(result2)
print('')


# sort list
Number = [1, 4, 7, 8, 6, 5, 9, 8]
Number.sort()
print(Number)

# descending list
letter = ["a", "s", "d", "f", "g", "h"]
letter.sort(reverse=True)
print(letter)

# reverse list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print("")


# copy list
num1 = [1, 2, 3, 5, 6, 7]
num2 = num1.copy() #copy method
print("Number2:", num2)
print("Number1:", num1)
print(num1 == num2)

thislist = ["apple", "banana", "cherry"] #list method
mylist= list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"] #slice operator
mylist= thislist[:]
print(mylist)

print('')


# join list
n1 = [1, 2, 3]
l1 = ["m", "a", "r", "i", "a"]
j1 = n1 + l1
print("J1:", j1)

n1.extend(j1)
print("Merge with j1:", n1,"\n")


# sum 
s= [1,2,3,4]
print(sum(s))
