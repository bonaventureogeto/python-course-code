num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Select operation:")
print("1. Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

operation = input("Enter the number corresponding to the operation: ")

if operation == "1":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "2":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "3":
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid input")
