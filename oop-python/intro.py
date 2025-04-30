"""
Object-Oriented Programming (or OOP) is a
way to organize your code by creating objects that have both data and behavior.
Class -> blueprint for creating an object
Objects -> instance of a class
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.year} {self.brand} {self.model} is driving!")

    def stop(self):
        print("The car has stopped!")

my_car = Car("Tesla", "Model S", 2023)
your_car = Car("Toyota", "Corolla", 2022)

my_car.drive()
my_car.stop()
