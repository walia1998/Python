def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is  {kwargs[item]}")

marks(Ashish = 99, Sania  = 56, Prikshit = 99.9)

#If you want to use names with spaces, you'll need to pass a dictionary and unpack it like this:
marks(**{"Ashish Walia": 99, "Sania Walia": 56})
