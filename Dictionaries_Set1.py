'''Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''
dic = {
    "maria": 106,
    "faisal": "01778325027",
    "cat": "cute"
}

print("QUESTION 1")
user = input("Enter the key word: ")
print(dic[user], "\n")


'''Write a program to input eight numbers from the user and display all the unique 
numbers (once)
'''
numbSet = set()  # empty set

print("QUESTION 2")
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))
user = input("Enter number: ")
numbSet.add(int(user))

print(numbSet, "\n")


'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.
'''
EmptyDic = {}

print("QUESTION 3")
name = input("Enter your name: ")
lang = input("Enter the language: ")
EmptyDic.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter the language: ")
EmptyDic.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter the language: ")
EmptyDic.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter the language: ")
EmptyDic.update({name: lang})

print(EmptyDic, "\n")
