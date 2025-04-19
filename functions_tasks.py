"""
write a function that adds up 3 numbers
write a function that checks if a number is even
write a function that takes two strings and prints them combined
"""

def addition(a, b, c):
    return a + b + c

result = addition(1, 3, 5)
print(result)

def even(number):
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print("Number is odd")

even_number = int(input("Enter number to check if even: "))

even(even_number)


def sum_string(str1, str2):
    print(f"{str1}, {str2}")

sum_string("Hello", "World!")
