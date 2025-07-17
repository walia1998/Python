from functools import reduce

numbers = [1,2,6,5,9,8]

def sum(a, b):
    return a + b

c = reduce(sum, numbers)
print(c)
