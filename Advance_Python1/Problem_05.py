# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)
with open("Tables.txt", "a") as f:
    # table k add krb text file e & str e convert
    f.write(f"Table of {n} is: {str(table)}\n")
