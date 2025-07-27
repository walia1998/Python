def very_slow_func():
    print("Very slow func")
    print("Very slow func")
    print("Very slow func")
    print("Very slow func")
    print("Very slow func")
    print("Very slow func")
    return 8


if((a:=very_slow_func())>10):
    print(a)

else:
    print("it's not greater then 10")



while(data:= input("please enter the data: ")):
    print(data)
    if data == "q":
        break