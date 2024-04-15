print("----------------------------------------------")
# --------------------- while loops ---------------------
# execute some code WHILE some condition remains true
# -------------------------------------------------------

# name = input("Enter your name: ")

# while not name:
#     print("You did not enter your name")
#     name = input("\nPlease enter your name: ")

# print(f"Hello {name}")

# -------------------------------------------------------

# food = input("Enter a food you like (press q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (press q to quit): ")

# print("Bye")

# -------------------------------------------------------

num = int(input("Enter a number between 1 - 10\n> "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1 - 10\n> "))

print(f"Your number is {num}")
