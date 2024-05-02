print("----------------------------------------------")
# --------------------- scope resolution ---------------------
# ------------------------------------------------------------
# variable scope: wher a variable is visible and accessible
# scope resolution:  (LEGB) Local -> Enclosed -> Global -> Built-in


# # Local
# def func1():
#     x = 1
#     print(x)


# def func2():
#     x = 2
#     print(x)


# func1()
# func2()


# ------------------------------------------------------------
# # Enclosed
# def func1():
#     x = 1

#     def func2():
#         # x = 2
#         print(x)

#     func2()


# func1()

# ------------------------------------------------------------
# # Global
# x = 3


# def func1():
#     print(x)


# def func2():
#     print(x)


# func1()
# func2()

# ------------------------------------------------------------
# Built-in
# rem. LEGB

from math import e


def func1():
    print(e)


e = round(e, 3)

func1()
