try:
    f = open("aashu.txt", "r")

    for line in f:
        print(line)
    f.close()
except FileNotFoundError:
    print("File not found")
    

    