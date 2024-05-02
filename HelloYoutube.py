print("----------------------------------------------")

try:
    with open("tst.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

# check whether file is closed
# print(file.closed)
