# try:
#     f = open("aashu.txt", "r")

#     content = f.read()
#     print(content)
#     f.close()
# except FileNotFoundError:
#     print("File not found")

try:
    with open("aashu.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found")

# No need to write f.close() because file is already closed by default.