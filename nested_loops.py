print("----------------------------------------------")
# --------------------- nested loops ---------------------
# A loop within another loop (outer, inner)
# --------------------------------------------------------

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# --------------------------------------------------------

rows = int(input("Enter the # of rows:\n> "))
columns = int(input("Enter the # of columns:\n> "))
symbol = input("Enter a symbol to use:\n> ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
