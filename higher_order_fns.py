print("----------------------------------------------")
# --------------------- higher order function ---------------------
# -----------------------------------------------------------------
# a fn that either: 1. accepts a fn as an argument
#                   2. returns a fn *(fns are treated as objects in python)

# # (1)
# def loud(text):
#     return text.upper()


# def quiet(text):
#     return text.lower()


# def hello(func):
#     text = func("Hello")
#     print(text)


# hello(loud)
# hello(quiet)


# -----------------------------------------------------------------
# (2)
def divisor(x):
    def dividend(y):
        return y / x

    return dividend


divide = divisor(2)
print(divide(10))
