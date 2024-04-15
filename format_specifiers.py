print("----------------------------------------------")
# --------------------- format specifiers ---------------------
# format specifiers: {value:flags} format a value based on what
#                    flags are inserted
# .(number)f -> round to that many decimal places (fixed point)
# :(number) -> allocate that many spaces
# :03 -> allocate and zero pad that many spaces
# :< -> left justify
# :> -> right justify
# :^ -> center align
# :+ -> use a plus sign to indicate positive values
# := -> place sign to leftmost position
# :  -> insert a space before positive numbers
# :, -> comma separator

price1 = 30000.14159
price2 = -9871.65
price3 = 12.34

# print(f"Price1: ${price1:.2f}")
# print(f"Price2: ${price2:.2f}")
# print(f"Price3: ${price3:.2f}")

# print(f"Price1: ${price1:10}")
# print(f"Price2: ${price2:10}")
# print(f"Price3: ${price3:10}")

# print(f"Price1: ${price1:010}")
# print(f"Price2: ${price2:010}")
# print(f"Price3: ${price3:010}")

# print(f"Price1: ${price1:+}")
# print(f"Price2: ${price2:+}")
# print(f"Price3: ${price3:+}")

# print(f"Price1: ${price1: }")
# print(f"Price2: ${price2: }")
# print(f"Price3: ${price3: }")

print(f"Price1: ${price1:+,.2f}")
print(f"Price2: ${price2:+,.2f}")
print(f"Price3: ${price3:+,.2f}")
