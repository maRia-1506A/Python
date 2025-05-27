# user defined function
def Minus():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    sub = x-y
    print(sub)


Minus()


# function defination with arguments
def Plus(name, ending):
    print("\nGood morning, "+name)
    print(ending)


Plus("User", "Thanks")  # function call


# return value
def Plus1(name, ending):
    print("\nGood morning, "+name)
    print(ending)
    return 7


a = Plus1("Python", "Hey")
print(a)  # return value varialbe er mddhe ase


#  default arguments
def day(opening, ending="Thank you"):
    print(f"Good day,{opening}")
    print(ending)


day("Maria")
day("Faisal", "Welcome\n")
