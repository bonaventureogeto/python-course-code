from utils import greet

# # not modular
# print("Hello, what's your name: ")
# name = input()
# print(f"Nice to meet you, {name}")

# # modular
# def greet_user():
#     name = input("Hello, enter your name: ")
#     print(f"Nice to meet you, {name}")

# greet_user()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print(add(2, 4))
    print(subtract(3, 6))

main()
print(greet("Bonaventure"))

# PEP8 - Python's style guide
# Flake8
