print("----------------------------------------------")
# --------------------- modules ---------------------
# ---------------------------------------------------
# A file containing code you want to include in you program
# use "import" to include a module (built-in or your own)
# useful to break up a large program resuable seperate files

# import math

# # import math as m
# # from math import e

# a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e**a)
# print(math.e**b)
# print(math.e**c)
# print(math.e**d)
# print(math.e**e)

# ---------------------------------------------------
# create a module
import example

result = example.pi
square = example.square(3)
cube = example.cube(3)
circum = example.circumference(7)
area = example.area(7)


print(result)
print(square)
print(cube)
print(circum)
print(area)
