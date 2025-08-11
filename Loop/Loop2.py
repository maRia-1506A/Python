'''Write a program to print the following star pattern.
  *
 * * *
* * *** for n = 3
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n-i), end="")  # space print
    print("*" * (2*i-1), end="")  # star print
    print("")


'''Write a program to print the following star pattern:
*
**
* * * for n = 3
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    print("*" * (i), end="")  # star print
    print("")


'''Write a program to print the following star pattern.
* * *
*   * for n = 3
* * * 
'''
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if (i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

