class Animal: # Parent Class (SuperClass)
    location = "Australia"

    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal generic sound")


class Dog(Animal): # it’s a child class or subclass
    def speak(self):
        return "Woof!"
    
d = Dog("Bruno")
print(d.speak())
        