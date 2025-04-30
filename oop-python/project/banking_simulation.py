"""
build a simple command-line banking system where users can:
    1. create bank accounts
    2. check balances
    3. deposit/withdraw money
    4. transfer funds
all while practicing core Python and OOP concepts.
"""


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, password, initial_deposit):
        pass

    def find_account(self, acc_number):
        pass

        # Additional bank-wide methods


class Account:
    def __init__(self, acc_number, name, password, balance=0):
        self.acc_number = acc_number
        self.name = name
        self.__password = password
        self.__balance = balance

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def check_balance(self, password):
        pass

    def transfer(self, target_account, amount, password):
        pass
