print("----------------------------------------------")
# --------------------- filter ---------------------
# --------------------------------------------------
# creates a collection of elements from an iterable for which a fn returns true
# filter(fn, iterable)

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20),
]

drinking_buddies = list(filter(lambda data: data[1] >= 18, friends))

for i in drinking_buddies:
    print(i)
