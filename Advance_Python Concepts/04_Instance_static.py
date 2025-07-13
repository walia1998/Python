class Employee:
    Company = "Samsung"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
     

    #Instance Method (default)
    def  print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    
    #static Method
    @staticmethod
    def sum(a,b):
       return a+b


    #class method
    @classmethod
    def print_company(cls):
        print(cls.Company)
    #change Method
    @classmethod
    def change_company(cls, new_company):
        cls.Company = new_company
        # print(cls.Company)



e1 = Employee("Ashish Walia", 80000)
e2 = Employee("Sania Walia", 80000)

# e1.print_info()
# e2.print_info()
#print(e1.sum(2,3))

print(Employee.Company)
e1.change_company("Hp")
print(Employee.Company)
# e1.print_company()
# e1.change_company("Acer")