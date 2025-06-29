#Decorator is a function that takes a function, it creates  a new function inside the body(wrapper). Then it creates a new function

def Decorator(func):
    def Wrapper(a):
        print("Hii, i am going to execute a function.....")
        func(a)
        print("I've executed the function")
    return Wrapper


@Decorator 


def say_hello(a):
    print(f"Hello! {a}")
say_hello("Sania ji ")


'''
The @Decorator syntax tells Python:

Take say_hello

Pass it into the Decorator function

Replace say_hello with whatever Decorator returns

'''
# f = Decorator(say_hello)
# f()