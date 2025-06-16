a = {1,55,69,2,3,46}

b = {4,6,8,44,68,46,55}


c = a.union(b) #contains all the elements in a along with all the elements in b.
print(c)


d = a.intersection(b) #Contains the only elements that are presents in a as well as b
print(d)

e = a.difference(b)
print(e)