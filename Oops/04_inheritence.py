class Animal: # Parent Class (SuperClass)
    location = "Australia"

    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking Now.......")


class Dog(Animal): # it’s a child class or subclass
    def speak(self):
        super().speak() # We are using the speak function from the parent class. 
        return "Woof!"
    
d = Dog("Bruno")
print(d.speak())


class Cat(Animal):
    def speak(self):
        return "Meow"
    
c = Cat("Sania")
print(c.speak())
        