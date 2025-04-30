# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Invalid amount or insufficient funds!")

    def get_balance(self):
        return self.__balance

# create account

account = BankAccount(1000)

account.deposit(250)
account.withdraw(500)

print(f"Current balance: ${account.get_balance()}")

# print(account.__balance) # will raise an AttributeError


"""
Create a Vehicle class and a Car class that inherits from it.
Make sure the Car class has a provate attribite like __fuel_level
and methods to add fuel and check fuel level

Post your code in the comments or on discord
"""
