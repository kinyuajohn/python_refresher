print("----------------------------------------------")
# --------------------- 2D Lists ---------------------
# ----------------------------------------------------
# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# groceries = [
#     ["apple", "orange", "banana", "coconut"],
#     ["celery", "carrots", "potatoes"],
#     ["chicken", "fish", "turkey", "beef"],
# ]

# # print(groceries[2][2])  # turkey

# count = 1
# for collection in groceries:
#     if count <= len(groceries):
#         print(f"Collection {count}:", end=" ")
#         count += 1
#     for food in collection:
#         print(food, end=" ")

#     print()

# ----------------------------------------------------
# 2D Keypad
num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")

    print()
