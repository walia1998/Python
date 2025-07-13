# while True : 
    # try:
    #     a = int(input("Enter number 1 :"))
    #     b = int(input("Enter number 2 :"))
    #     print(f"The sum is {a / b}")    

    # except ValueError:
    #     print("Please dont perform bad typecast")

    # except ZeroDivisionError:
    #     print("please dont divide by 0")

    # except Exception as e :
    #     print("Some error has occured", e)




a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

if b == 0:
    raise ValueError("please dont divide by 0")

print(f"Please dont divide by zero")