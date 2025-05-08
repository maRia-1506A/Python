'''
{key : value}
Ordered, Changeable & Not allow duplicates
'''

Info1 = {
    "Maria": {
        "name": "Maria",
        "location": "Dhaka",
        "roll": 106,
        "number": "01778326029"
    },
    "Faisal": {
        "name": "Faisal",
        "location": "Dhaka",
        "roll": 200,
        "number": "01736325027"
    },
    "year": 2025
}
print(type(Info1))
print(Info1["Maria"])
print(Info1["Faisal"]["number"])
print('')

# access dict items
print(Info1["year"])

a = Info1.get("Faisal")  # get method
print(a)

print(Info1.keys())  # keys name(parent key)

print(Info1.values())  # values name
print('')

# change/add dict items
Info1["year"] = 1971
print(Info1["year"])

Info1.update({"Faisal": "Faisal has 1 sister"})  # update method
print(Info1["Faisal"])
print('')

# remove dict items
Info1.pop("Faisal")
print(Info1)

Info1.popitem()  # remove last item
print(Info1)
# del & clear is same as list
print('')


# loop dict items
Info2 = {
    "Zannatul": {
        "name": "Zannatul",
        "location": "Dhaka",
        "roll": 1025,
        "number": "123654789"
    },
    "Farzana": {
        "name": "Farzana",
        "location": "Dhaka",
        "roll": 1599,
        "number": "123456789"
    },
    "year": 1111
}

# key name
for i in Info2:
    print(i)

for k in Info2.keys():  # key method
    print(k)

# value name
for j in Info2.values():
    print(j)

# both keys & values
for dic in Info2.items():
    print(dic)
print('')


# copy dictionaries
Info3 = {
    "sum1": 10,
    "sum2": 20,
    "sum3": 30,
}
c1 = Info3.copy() #copy method
print(c1)
print(c1 == Info3)

c2 = dict(Info3) #dict method
print(c2)
print(c2 == Info3)
