''' 
Unchangeable, Unordered and unindexed
Duplicates not allowed
'''

set1 = {1, 2, 3, '3', 4, 4}
print('Length:', len(set1))
print(set1)

# access set item
for i in set1:  # for all item
    print(i)

print('9 is in the list:', 9 in set1)  # specific item
print('')


# add set items
set2 = {'m', 'a', 'r', 'i', 'a'}
set2.add('A')
print(set2)

# update item
tuple2 = (1, 2, 3, 4, 5)
set2.update(tuple2)
print("Updated set", set2)
print(type(set2))
print('')


# remove set items
set3 = {10, 20, 40, 30, 50, 70}
print(set3)
set3.remove(70)
print(set3)

set3.discard(100)  # discard method
print(set3)

set3.clear()
print(set3)
print('')


# loop set items
set4 = {"maria", "afridi", "mishka", "aziz", "efath"}
for i in set4:
    print(i)
print('')


# join set items
set5 = {"a", "b", "c"}
set6 = {1, 2, 3}
print(set5.union(set6))  # can add multiple set

set6.update(set5)  # update method
print(set6)

# join multiple sets
myset = set4 | set5 | set6
print("Myset:",myset)
