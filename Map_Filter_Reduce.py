from functools import reduce
# Map example
l = [1, 2, 3, 4, 5]

square= lambda x: x*x

squareByMap = map(square, l)
print(list(squareByMap))  #need to convert into list


# Filter example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven= filter(even, l)
print(list(onlyEven))


# Reduce example
def sum(a,b):
    return a+b
  
def multiply(x,y):
  return x*y

print(reduce(sum,l))
print(reduce(multiply,l))
'''
1   2   3   4
 \  /
   3    3   4
    \  /
      6     4
       \   / 
         10
'''