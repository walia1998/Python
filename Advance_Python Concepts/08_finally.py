
def divided(a,b):
    try:
        c = a/b
        print(c)
        return c 


    except Exception as e:
        print(e)
        return none

    finally: 
       print("This is always executed no matter if try completly executed or not   ")


a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
divided(a,b)