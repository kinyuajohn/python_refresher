print("----------------------------------------------")
# --------------------- *args_**kwargs ---------------------
# ----------------------------------------------------------
# Arbitrary arguments
# *args: allows you to pass multiple non-key arguments
# **kwargs: pass multiple keyword args.
# *: unpacking operator


# ----------------------------------------------------------
# # *args
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# # def add(*nums):
# #     total = 0
# #     for num in nums:
# #         total += num
# #     return total

# print(add(1, 2, 3, 4, 5))


# ----------------------------------------------------------
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Dr.", "Spongebob", "Harold", "Squarepand", "III")


# ----------------------------------------------------------
# # **kwargs
# def print_address(**kwargs):
#     # for value in kwargs.values():
#     #     print(value)

#     # for key in kwargs.keys():
#     #     print(key)

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="123 Fake St.", apt="100", city="Detroit", state="MI", zip="54321")


# ----------------------------------------------------------
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label(
    "Dr.",
    "Spongebob",
    "Harold",
    "Squarepants",
    "III",
    street="123 Fake St.",
    apt="#100",
    city="Detroit",
    state="MI",
    zip="54321",
)
