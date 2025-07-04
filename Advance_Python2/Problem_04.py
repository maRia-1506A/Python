# 4. Write a program to filter a list of numbers which are divisible by 5.
def divisible(n):
    if (n % 5 == 0):
        return True
    return False


li = [1, 565, 24, 169, 125, 458, 90]
div = list(filter(divisible, li))
print(div)
