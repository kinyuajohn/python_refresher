print("----------------------------------------------")

# --------------------- Intro ---------------------
# print("I love pizza")

# --------------------- Variables ---------------------
# age = 21
# print("You are " + str(age) + " years old")
# print("You are", age, "years old")
# print(f"You are {age} years old")

# x, y, z = 1, 2, 3
# print(x)
# print(y)
# print(z)

# x = y = z = 1
# print(x)
# print(y)
# print(z)

# --------------------- typecasting ---------------------
# name = "Jane"
# name2 = ""
# age = 30
# gpa = 1.9
# student = True

# print(type(name))

# print(float(age))

# gpa = int(gpa)
# print(gpa)

# student = str(student)
# print(student, type(student))

# age = bool(age)
# print(age)

# name2 = bool(name2)
# print(name2)

# --------------------- user input ---------------------
# name = input("Enter your name: ")
# age = int(input(f"How old are you {name}: "))
# age = age + 1

# print(f"Hello {name}. You are {age} years old")

# --------------------- math ---------------------
# friends = 5
# friends *= 3
# friends **= 2  # friends = friends ** 2
# remainder = friends % 4

# print(friends)
# print(remainder)

# print(abs(-3.14)) # distance from 0

# import math

# radius = float(input("Enter the radius of a circle (cm): "))

# circum = 2 * math.pi * radius
# area = math.pi * math.pow(radius, 2)

# print(f"Circumference: {round(circum, 2)}cm\nArea: {round(area, 2)}cm^2")

# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side c = {c}")

# --------------------- if statements ---------------------
# name = input("Please enter your name: ")

# if name:
#     print(f"Your name is {name}")
# else:
#     print("You did not enter your name!")

# # Weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilogram or Pounds (K / L): ")

# if unit == "L":
#     weight *= 2.205
#     unit = "Kgs"
#     print(f"You are {round(weight, 2)} {unit}")
# elif unit == "K":
#     weight /= 2.205
#     unit = "Lbs"
#     print(f"You are {round(weight, 2)} {unit}")
# else:
#     print(f"{unit} is not valid!")

# # Temp converter
# unit = input("Is the temp in Celcius or Fahrenheit (C / F): ")
# temp = float(input("What's the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}°F")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1)
#     print(f"The temperature in Celcius is: {temp}°C")
# else:
#     print(f"{unit} is an invalid unit of measurement")

# --------------------- logical operators ---------------------
# temp = 20
# sunny = True

# if temp <= 0 or temp >= 30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")

# if not sunny:
#     print("It is cloudy outside")
# else:
#     print("It is sunny outside")

# --------------------- string methods ---------------------
# name = input("Enter your full name: ")
# phone_number = input("Enter your phone #: ")

# result = name.find(" ") # find first occurrence, -1 of no occurrence
# result = name.rfind("q")  # find last occurrence, -1 of no occurrence
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")

# print(phone_number)
# print(help(str))

##### Exercise --- validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username muct not contain digits

# username = input("Enter a username: ")

# if len(username) < 4:
#     print("Your Username can't be less than 4 characters")
# elif len(username) > 12:
#     print("Your Username can't be more than 12 characters!")
# elif not username.find(" ") == -1:
#     print("Your Username can't contain spaces!")
# elif not username.isalpha():
#     print("Your Username can't contain numbers!")
# else:
#     print(f"Welcome {username}")

# --------------------- string indexing ---------------------
# [start : end : step]
# credit_number = "1234-5678-9101-1121"

# print(credit_number[0])
# print(credit_number[:4])  # last number is exclusive (not included)
# print(credit_number[-1])  # get last index
# print(credit_number[::2])  # print every 2nd character

##### get last 4 digits of credit_number
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

##### reverse credit_number
# credit_number = credit_number[::-1]
# print(credit_number)

##### string slicing
# email = input("Enter your email: ")
# index = email.index("@")
# username = email[:index]
# domain = email[index + 1 :]

# print(f"Username: {username}\nDomain: {domain}")
