def sum(a,b):

    c = a + b #here a & b are local variables
    x = 66 # local variable 
    return c

x = 65 #here x is global variable

print(sum(4,5))
print(x)


