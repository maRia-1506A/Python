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
