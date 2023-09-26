class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1

def add(num1: int, num2: int) -> int:
    return num1 + num2

def subtract(num1: int, num2: int) -> int:
    return num1 - num2

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

def divide(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
