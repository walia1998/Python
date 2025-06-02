def add(a,b):
    return a + b

c = add(5, 6)

print(c)



def add(a, b , plus=0):
    x = a + b + plus
    return x


d = add(6,8,9)
print(d)