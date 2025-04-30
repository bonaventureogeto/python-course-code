# inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound!")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows!")

dog = Dog("BUDDY")
cat = Cat("Whiskers")

dog.speak()
dog.bark()

cat.speak()
cat.meow()
