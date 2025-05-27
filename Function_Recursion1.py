# Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(f):
    return 5*(f-32)/9


f = int(input("Enter the temparature in F: "))
c = c_to_f(f)
print(f"{round(c, 2)}°C\n")


# Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(n)=1+2+3+....+(n-1)+n
sum(n)= sum(n-1)+n
'''


def recursive_sum(n):
    if (n == 1):
        return 1
    return recursive_sum(n-1)+n


n = int(input("Enter natural number: "))
print(f"Sum of first {n} natural number is: {recursive_sum(n)}\n")


# Write a python function to print first n lines of the following pattern:
'''
***
** - for n = 3
*
'''


def pattern(n):
    if (n == 0):
        return  # func stops
    print("*" * n)
    pattern(n-1)


pattern(5)


