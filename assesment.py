# import array as arr

# my_arr = arr.array("i", [1, 2, 4, 5])
# print(my_arr)
# print(type(my_arr))

# ---------------------------------------------------------------
# def fun(i):
#     i[0] = 3


# i = [1, 2, 3, 4]
# fun(i)
# print(i)

# ---------------------------------------------------------------
# def fun(i):
#     i = [3, 2, 3, 4]


# i = [1, 2, 3, 4]
# fun(i)
# print(i)

# ---------------------------------------------------------------
# import random

# print(random.random())
# print(random.randrange(1, 10))

# ---------------------------------------------------------------
# var = "Si mplile arn"

# for i in var:
#     if i == " ":
#         pass
#     else:
#         print(i, end="")

# ---------------------------------------------------------------
# my_string = "abscd123"

# print(my_string.isalnum())

# ---------------------------------------------------------------
# my_string = "Hey john. How are you, john"

# print(my_string.replace("john", "John", 2))

# ---------------------------------------------------------------
# lst = [1, 2, 3]
# lst.append(4)
# print(lst)

# lst = [1, 2, 3]
# lst.extend([4, 5, 6])
# print(lst)


# ---------------------------------------------------------------
# def add(a, b):
#     """This function adds two numbers."""
#     sum = a + b
#     return sum


# sum = add(10, 20)

# # print("Accessing docstring method:", add.__doc__)

# print("Accessing docstring method 2:", end="")

# help(add)

# ---------------------------------------------------------------
# var = "Red,Blue,Green,Orange"

# lst = var.split(",")
# print(lst)


# ---------------------------------------------------------------
# def fun(*var):
#     for i in var:
#         print(i)


# fun(1)
# fun(1, 25, 6)

# ---------------------------------------------------------------
# print(__name__)

# ---------------------------------------------------------------
# add = lambda x, y: x + y
# print(add(4, 5))


# ---------------------------------------------------------------
# def count_to(n):
#     num = 1
#     while num <= n:
#         yield num  # This makes our fn a generator
#         num += 1


# # use the generator
# for number in count_to(10):
#     print(number)


# ---------------------------------------------------------------
# class Mother:
#     def mother_speak(self):
#         print("Mother speaking")


# class Father:
#     def father_speak(self):
#         print("Father speaking!")


# class Child(Mother, Father):
#     def child_speaking(self):
#         print("Child speaking!")


# child = Child()
# child.father_speak()
# child.mother_speak()
# child.child_speaking()


# ---------------------------------------------------------------
# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")


# say_hello()

# -------------------- * switch numbers * --------------------
# x = 5
# y = 10

# x, y = y, x
# print(f"x = {x}, y = {y}")


# -------------------- * Prime Number * --------------------
# def is_prime(num):
#     """Check for prime numbers"""
#     # Check if the number is less than 2
#     if num < 2:
#         return False

#     # Check for factors from 2 to the sq_root of the number
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False

#     # If no factors are found, the number is prime
#     return True


# # Get user input
# num = int(input("Enter a number: "))

# # Check if the number is prime
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# -------------------- * Factorial * --------------------
# Example 1
# def compute_factorial(num):
#     factorial = 1
#     if num < 0:
#         print("Sorry, factorial does not exist for -ve numbers.")
#     elif num == 0:
#         print("The factorial of 0 is 1.")
#     else:
#         for i in range(1, num + 1):
#             factorial = factorial * i
#         print(f"The factorial of {num} is {factorial}.")


# compute_factorial(int(input("Enter a number: ")))

# Example 2
# memo = {}

# def factorial_memory(n):
#     if n == 0:
#         return 1
#     if n in memo:
#         return memo[n]
#     memo[n] = n * factorial_memory(n - 1)
#     return memo[n]


# factorial = factorial_memory(int(input("Enter a number: ")))
# print(factorial)

# print(memo)

# -------------------- * random number* --------------------
# import random

# # Gives a random float number btwn 0 and 1
# num = random.random()
# print(num)

# # Gives a random float in specified range
# num = random.uniform(1, 100)
# print(num)

# # random interger in specific ranger
# num = random.randint(1, 100)
# print(num)

# # random number in ranger with incremental steps
# num = random.randrange(0, 100, 2)
# print(num)

# # series of random numbers
# numlist = random.sample(range(0, 100), 4)
# print(numlist)


# -------------------- * fibonacci * --------------------
# print first 10 numbers of fibonacci
# def print_fibonacci(num):
#     a, b = 0, 1
#     if num < 1:
#         print("null")
#     elif num == 1:
#         print(a)
#     elif num == 2:
#         print(a)
#         print(b)
#     elif num > 2:
#         print(a)
#         print(b)
#         # Generate next number in the series
#         for _ in range(num - 2):
#             c = a + b
#             # Update a and b to prepare for next itereation
#             a, b = b, c
#             # Print the next term in the series
#             print(c)


# print_fibonacci(int(input("Enter a number: ")))

# -------------------- * square root * --------------------
# # Example 1
# num = float(input("Number: "))

# num_sqrt = num**0.5
# print(f"The square root of {num:.2f} is {num_sqrt:.2f}")
# 25

# # Example 2: complex number
# import cmath

# num = 1 + 2j
# # Take input from user
# # num = eval(input("Enter a number: "))

# num_sqrt = cmath.sqrt(num)
# print(f"The square root of {num} is {num_sqrt:.3f}+{num_sqrt.imag:.3f}j")

# -------------------- * interchange elements in list * --------------------
# # Initalize empty list
# a = []

# # Taker user input for the number of elements in the list
# n = int(input("Enter the number of elements in list: "))

# # Loop to get user input for each element and append to the list
# for x in range(0, n):
#     element = int(input(f"Enter element {str(x + 1)}: "))
#     a.append(element)


# # Swap the first and last elements of the list
# a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
# print("New list is:")
# print(a)

# -------------------- * leap year * --------------------
# year = int(input("Enter a year: "))

# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print(f"{year} is a leap year")
# # year divided by 4 and not divided by 100 is a leap year
# elif (year % 4 == 0) and (year % 100 != 0):
#     print(f"{year} is a leap year")
# # if not divided by both 400 and 4 not a leap year
# else:
#     print(f"{year} is a not a leap year")

# -------------------- * armstrong number * --------------------
# # number that is eqaul to the sum of the cubes of its own digits

# num = int(input("Enter a number: "))

# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     sum = sum + (digit**3)
#     temp = temp // 10

# if num == sum:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")

# -------------------- * palindrome * --------------------
# # A word, number, phrase, etc that reads the same
# # backwards or forwards
# # i.e MADAM, RACECAR
# my_str = input("Enter a string: ")

# # make it suitable for caseless comparison
# my_str = my_str.casefold()

# # reverse the string
# rev_str = "".join(reversed(my_str))

# # check if string is equal to it's reverse
# if my_str == rev_str:
#     print(f"{my_str.upper()} is Palindrome")
# else:
#     print(f"{my_str.upper()} is not Palindrome")
