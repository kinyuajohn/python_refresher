print("----------------------------------------------")
# --------------------- reduce ---------------------
# --------------------------------------------------
# applys a fn to an iterable and reduce it to a single cumulative value
# performs fn on first two elements and repeats process until 1 value remains
# reduce(fn, iterable)

import functools

# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y: x + y, letters)

# print(word)

# --------------------------------------------------
factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)

print(result)
