# Lesson 19.
"""
Create a class called BankAccount to represent a basic bank account. The class should
have the following attributes:
1. owner: The name of the account owner.
2. balance: The current balance of the account.
Implement the following methods:
1. __init__(self, owner, balance): Initializes the BankAccount object with the
owner's name and initial balance. Ensure that the balance is a non-negative
integer.
2. get_balance(self): Returns the current balance of the account.
3. deposit(self, amount): Adds the specified amount to the account balance.
Ensure that the amount is a positive integer.
4. withdraw(self, amount): Subtracts the specified amount from the account
balance. Ensure that the amount is a positive integer and does not exceed the
current balance.
Additionally, use @property and @attribute.setter to encapsulate the balance
attribute and enforce validation rules.
"""


class BankAccount:
    def __init__(self, account_owner, current_balance):
        self.owner = account_owner
        if current_balance < 0:
            raise ValueError("Not valid balance: the balance should be higher than 0")
        else:
            self.__balance = current_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            raise ValueError("Not valid deposit amount: higher than 0 acceptable")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Invalid withdraw: higher than 0 acceptable')
        else:
            if amount <= self.__balance:
                self.__balance -= amount
                return self.__balance
            else:
                raise ValueError('Insufficient balance')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, specific_balance):
        if specific_balance >= 10000:
            self.__balance = specific_balance
        else:
            raise ValueError('Insufficient balance: min 10.000 accepted')


accountA = BankAccount("Tigran Tigranyan", 50000)
print(accountA.get_balance())
print(accountA.deposit(5000))
print(accountA.withdraw(50000))
accountA.balance = 11000
print(accountA.balance)
print(accountA.withdraw(5000))
