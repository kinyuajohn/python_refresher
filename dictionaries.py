print("----------------------------------------------")
# --------------------- Dictionaries ---------------------
# --------------------------------------------------------
# A collection of {key: value} pairs
# ordered and changeable
# No duplicates

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# --------------------------------------------------------
# print(dir(capitals))

# print(capitals.get("USA"))  # Washington D.C.
# print(capitals.get("Japan"))  # None

# if capitals.get("Japan"):
#     print("Capital exists")
# else:
#     print("Capital doesn't exist")

# --------------------------------------------------------
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals)

# --------------------------------------------------------
# capitals.pop("China")
# capitals.popitem()  # removes last item
# capitals.clear()
# print(capitals)

# --------------------------------------------------------
# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# --------------------------------------------------------
# for value in capitals.values():
#     print(value)

# --------------------------------------------------------
# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
