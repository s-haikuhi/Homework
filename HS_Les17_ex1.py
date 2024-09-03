# Lesson 17.
"""
Define a class named BankAccount with an __init__ method that initializes two
instance variables: account_holder and balance.

The class has methods like deposit and withdraw, each of which takes an amount as
an argument and updates the account balance accordingly. These methods also
include checks for valid input and available funds.
The get_balance method allows you to retrieve the account balance.

We create an Object of the BankAccount class called account1 with an initial balance
of $1000.
We deposit $500 and withdraw $200 from the account and print the account
information.
"""


class BankAccount:
    def __init__(self, account_holder, balance):
        self.name = account_holder
        self.balance = balance

    def my_deposit(self, amount: int, interest_rate: int, duration_days: int, income_tax=10):
        try:
            self.balance += amount + (round(amount * interest_rate / 100 * duration_days / 365) -
                                      round(
                                          amount * interest_rate / 100 * duration_days / 365 * income_tax / 100))
            return self.balance
        except TypeError as e:
            print(f'Only the amount in numbers accepted: {e}')

    def my_withdraw(self, amount: int):
        if self.balance - amount < 0:
            raise Exception("Non-sufficient funds")
        else:
            self.balance -= amount
            return self.balance

    def get_balance(self):
        return self.balance


account1 = BankAccount("account1", 1000)

print(account1.my_deposit(500, 0, 0, 0))
print(account1.my_withdraw(2000))
print(account1.get_balance())

# Output: Exception: Non-sufficient funds
