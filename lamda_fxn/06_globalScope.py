def sum(a, b):
    print("Hey, I am Invincible")
    c = a + b
    global z #Please modify global scope
    z = 56 # This will refer to global z and not create a local variable    
    return c

z = 95

print(sum(9,6))
print(z)
