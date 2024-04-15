print("----------------------------------------------")
# --------------------- lists, sets, tuples ---------------------
# ---------------------------------------------------------------
# List: [] ordered and changeable. Duplicates OK
# Set = () unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER#

# List
# fruits = ["apple", "orange", "banana", "coconut", "banana"]

# print(fruits[1::2])

# for fruit in fruits:
#     print(fruit)

# # methods available to a collection >>> dir(collection_name)
# print(dir(fruits))
# # print the description
# help(fruits)

# print(len(fruits))
# print("apple" in fruits)

# fruits[2] = "pinepple"
# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# fruits.insert(0, "pineapple")
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.reverse()  # reversed according to the order they appear
# print(fruits)

# fruits.clear()
# print(fruits)

# print(fruits.index("banana"))

# print(fruits.count("pineapple"))

# ---------------------------------------------------------------
# sets
# fruits = {"apple", "orange", "banana", "coconut"}

# print(len(fruits))
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() # remove an element
# fruits.clear()

# print(fruits)

# for fruit in fruits:
#     print(fruit)

# ---------------------------------------------------------------
# tuple
# fruits = ("apple", "orange", "banana", "coconut", "banana")

# print("pineapple" in fruits)
# print(len(fruits))
# print(fruits.index("orange"))
# print(fruits.count("banana"))

fruits = ["apple", "orange", "banana", "coconut", "banana"]
fruit2 = []

for fruit in fruits:
    fruit2.append(fruit)
    fruit_tuple = tuple(fruit2)
    print(fruit_tuple)


fruit_tuple2 = tuple(fruits)
print(f"Fruit Tuple 2:\n{fruit_tuple2}")

# # Creating myList with some random values in it
# myList = ['one', 2, 'three', 4, 'five']
# print(type(myList))

# # Converting a list to a tuple in python using for loop inside the tuple() function
# myTuple = tuple(i for i in myList)

# # Printing myTuple
# print(myTuple)
# print(type(myTuple))
