# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    

a = [ 1,5,9,8,89,5,6,78,45,32,12,11,47]

# new = list(filter(is_greater_than_9, a))

new  = list(filter(lambda x : x>9, a))
print(new)