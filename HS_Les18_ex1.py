# Lesson 18. Class Inheritance
"""
Exercise: Bank Account Hierarchy
Create a hierarchy of classes representing different types of bank accounts. Start
with a base class called BankAccount. Then, create two subclasses,
SavingsAccount and CheckingAccount. Each subclass should inherit from the
BankAccount class.
● The BankAccount class should have the following attributes and methods:
○ Attributes: account_number, balance
○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
● The SavingsAccount class should inherit from BankAccount and have an
additional attribute interest_rate. Override the deposit method to add
interest to the balance when a deposit is made.
● The CheckingAccount class should inherit from BankAccount and have an
additional attribute overdraft_fee. Override the withdraw method to deduct
the overdraft fee if a withdrawal causes the balance to go below zero.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def balance(self):
        return f"{self.account_number}'s final balance is {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount + (amount * self.interest_rate / 100)
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_fee):
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= amount + self.overdraft_fee
            return self.balance
        else:
            return self.balance - amount


account1 = SavingsAccount(8, 40000, 10)
account2 = CheckingAccount(8, 40000, 14000)
print(account1.deposit(4000))
print(account2.withdraw(41000))
