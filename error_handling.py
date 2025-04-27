# syntax
# print("Hello World"

# runtime
# x = 5 / 0

try:
    # code that might cause an KeyError
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result is {result}")
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")

# debugging

# def divide (a, b):
#     print(f"Dividing {a} by {b}")
#     return a / b

# divide(2, 5)

# tracebacks
# PEP8 guideline
# flake8
