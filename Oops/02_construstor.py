class Employee:

    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is {self.bond} years")




e = Employee("Ashish Walia", 80000, 4)
e.get_info()