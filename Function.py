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
def Plus1(num1, num2):
    return num1 + num2


num1 = int(input("\nEnter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(Plus1(num1, num2))


#  default arguments
def day(opening, ending="Thank you"):
    print(f"\nGood day,{opening}")
    print(ending)


day("Maria")
day("Faisal", "Welcome\n")
