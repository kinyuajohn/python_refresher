class Car:
    wheels = 4  # class variable
    make = "MAN"

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable (declared inside constructor)
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable
