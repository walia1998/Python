#Object : specific instance created from the template (class) for eg. from which contain the data for John doe.

#Class : class is a blueprint or a template. Eg. from for an eg that contain Name, Age, Electives,Father's name etc.


class Employee:
    company = "HP"

    def get_salary(self):  #here self is an object ot the class which is being created for eg as per this ( e is an object here so self represent to e)
        return 34000
    
e1 = Employee() #An Object of class employee is created here
print(e1.get_salary()) # Employee e's get salary method is called. 

e2 = Employee()
print(e2.company)
print(e2.get_salary())