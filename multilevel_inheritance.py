print("----------------------------------------------")
# --------------------- multilevel inheritance ---------------------
# ------------------------------------------------------------------
# when a derived (child) class inherits another derived (child) class


class Oraganism:
    alive = True


class Animal(Oraganism):
    def eat(self):
        print("This animal is eating.")


class Dog(Animal):
    def bark(self):
        print("This dog is barking.")


dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
