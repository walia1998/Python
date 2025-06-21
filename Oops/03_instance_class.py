class Employee:
    company = "Asus" # This is class Attribute.

    def __init__(self, name, salary, bond, company):
        self.name = name # create an instance attribute of name  and assign it with name 
        self.salary = salary
        self.bond = bond
        self.company = company 

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is {self.bond} years")




e = Employee("Ashish Walia", 80000, 4,"Tesla")
print(e.company) # Will always print instance attribute whenever present
print(Employee.company) # This will always create class attribute 