class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

        #This is the constructor.

        #When you write p1 = Point(3, 6), it saves x = 3 and y = 6 for p1.

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
     
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
      print(f"X is {self.x} and y is {self.y}")


p1 = Point(3,6)
p2 = Point(9,6)


p = p1.sum(p2) # Returns a new Point which is sum of p1 & p2
p = p1 + p2 # we overloadded  the +  operator by using __add__ method
p.print_point()