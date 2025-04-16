# operations and expressions in Python

# 5 + 3 returns 8
# hello + world returns hello world
import numbers
from token import EQUAL

a = 10
b = 3

# result = a ** b
# print(f"The result is {result}")

print(a == b) # equal to
print(a != b) # not equal
print(a < b) # less than
print(a >= b) # greater or equal to
print(a <= b) # less or equal to


# logical operators
print(a > 2 and b < 20) # logical and
print(a > 10 or b == 3)
print(not (a < b))

# assignment operators
score = 10 # assign value
score += 5 # add and reassign
score -= 9 # subtract and reassign

print(score)

# Task
"""
Ask a user for two numbers
print the sum
print the difference
check if they are EQUAL
reassign the value of the sum by 10
print a well formatted answer
"""
