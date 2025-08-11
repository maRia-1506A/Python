l = [10, 20, 30, 40]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# this can be simplified using enumerate function
# enumerate(iterable, start)
for index, item in enumerate(l, start=1):
    print(f"The item number at index {index} is {item}")
