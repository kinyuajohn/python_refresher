print("----------------------------------------------")
# --------------------- Functions ---------------------
# -----------------------------------------------------
# A block of reusable code
# Place () after the fn name to invoke it

# -----------------------------------------------------
# def happy_birthday(name, age):
#     print(f"Happy birthday {name}!")
#     print(f"You are {age} years old.")
#     print()


# happy_birthday("John", 20)
# happy_birthday("Joe", 10)
# happy_birthday("Sarah", 25)


# -----------------------------------------------------
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due on {due_date}")


# display_invoice("jkinyua", 42.56, "01/02")


# -----------------------------------------------------
# # return: a sttmt used to end a fn & send a result back to the caller
# def add(x, y):
#     z = x + y
#     return f"{x} + {y} = {z}"


# def subtract(x, y):
#     z = x - y
#     return f"{x} - {y} = {z}"


# def multiply(x, y):
#     z = x * y
#     return f"{x} * {y} = {z}"


# def divide(x, y):
#     z = x / y
#     return f"{x} / {y} = {z}"


# print(add(3, 2))
# print(subtract(1, 2))
# print(multiply(5, 7))
# print(divide(5, 9))


# -----------------------------------------------------
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"


full_name = create_name("john", "kINYUA")
print(full_name)
