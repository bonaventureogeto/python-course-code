def say_hello():
    print("Hello!")

def get_greeting():
    return "Hello!"

greet_var = get_greeting()
print(greet_var)

say_hello()

# lambda functions - this is a quick, throwaway function with no name

def double(x):
    return x * 2

# lambda version

double1 = lambda x: x * 2
add = lambda a, b: a + b

print(double1(4))
print(add(2, 4))

# challenge: write a lambda function that returns the square of a number
