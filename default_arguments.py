print("----------------------------------------------")
# --------------------- Default Arguments ---------------------
# -------------------------------------------------------------
# A default value for certain parameters
# Used when that argument is ommitted
# makes your functions more flexible, reduces # of arguments
# 1. positional 2. DEFAULT 3. keyword 4. arbitrary#

# -------------------------------------------------------------
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))
# -------------------------------------------------------------
import time


def count(end, start=0):
    for x in range(start, end):
        print(x, end=" ")
        time.sleep(1)

    print("DONE!")


count(30, 20)
