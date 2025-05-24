# Write a program to print multiplication table of a given number using for loop
print("Question 1")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n}*{i} = {n*i}")

print("Using while loop:")
i = 1
while i < 11:
    print(f"{n}*{i} = {n*i}")
    i += 1


# Write a program to greet all the person names stored in a list ‘l’ and which startswith S
l = ["Harry", "Soham", "Sachin", "Rahul"]
print("\nQuestion 2")
for name in l:
    if (name.startswith("S")):
        print(f"Welcome {name}\n")


# Write a program to find whether a given number is prime or not.
print("Question 3")
numb = int(input("Enter number: "))
for i in range(2, numb):
    if (numb % i) == 0:
        print("Number is not prime\n")
        break
else:
    print("Number is prime\n")


# Write a program to print multiplication table of n using for loops in reversed order.
print("Question 4")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n}*{11-i} = {n*(11-i)}")
