template = "Dear {}, you are awsome, take this {}$ bag."

a = "Ashish Walia"
a1 = 100000

# Method 1

s = template.format(a, a1)
print(s)

# Method 2
print(f"Dear {a}, you are awsome, take this {a1}$ bag.")