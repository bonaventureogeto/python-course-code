# def function_name(parameters):
#     # code block
import numbers

def greet(name): # function definition
    print(f"Hello, {name}!")

name = input("Enter a name: ")

greet(name) # function call

def add(a, b):
    return a + b

result = add(3, 6)
print(f"The sum is {result}")


def multiply(num1, num2):
    return num1 * num2

print(multiply(10, 23))


"""
write a function called square(num) that returns the square of a number
"""

def square(num):
    return num * num

output = square(30)

print(f"The square is {output}")


"""
write a function that adds up 3 numbers
write a function that checks if a number is even
write a function that takes two strings and prints them combined
"""
