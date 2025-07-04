# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

li = [11, 565, 3, 24, 169, 125, 458, 90]


def max(a, b):
    if (a > b):
        return a
    return b


print(reduce(max, li))
