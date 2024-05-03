print("----------------------------------------------")
# --------------------- class variables ---------------------
# -----------------------------------------------------------

from car2 import Car

# car_1 = Car("Chevy", "Corvette", 2021, "blue")
# car_2 = Car("Ford", "Mustang", 2022, "red")

# car_1.wheels = 2  # affects only car_1

# print(car_1.wheels)
# print(car_2.wheels)

# -----------------------------------------------------------
# print(Car.wheels)

# -----------------------------------------------------------
car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.wheels = 2  # affects all instances
# Car.make = "Scania"
car_1.make = "Mercedes"

print(car_1.wheels)
print(car_2.wheels)
print(Car.make)
print(car_1.make)
print(car_2.make)
