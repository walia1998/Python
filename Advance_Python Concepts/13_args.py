def sum(*args):
 # args will be a tuple of all the values passed to sum

    total = 0
    for item in args:
        total += item
    return total
    
print(sum(7,8,65,12,1))