

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name =  new_name
    


e = Employee("Ashish Walia", 80000)

print(e.first_name)
e.first_name = "sania"
print(e.salary)