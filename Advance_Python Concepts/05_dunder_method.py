class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name of the employee is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name:{self.name} \nsalary:{self.salary}"
    
    def __len__(self):
        return len(self.name) 
    

e = Employee("Ashish Walia", 80000)

print(e.name, e.salary)
print(str(e))
print(repr(e))
print(len(e))
