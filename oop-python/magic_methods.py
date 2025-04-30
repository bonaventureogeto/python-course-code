# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("Woof!")

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# my_dog = Dog("Buddy", 3)
# print(my_dog)

# class -> object -> method
# __init__, __str__, __len__, __add__, etc

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.pages} pages."

# create a book instance
book1 = Book("1984", "George Orwell", 328)
print(book1)

"""
create a Car class that uses __init__ to set the brand
and year, and uses __str__ to print something like:
    'Toyota made in 2021'
"""
