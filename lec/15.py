"""Object-Oriented Programming"""

class Account:
    """An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('Brian')
    >>> a.holder
    'Brian'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10

    >>> a = Account('Brian')
    >>> b = Account('Marvin')
    >>> a.holder
    'Brian'
    >>> b.holder
    'Marvin'
    >>> a is b
    False
    >>> c = a
    >>> c is a
    True

    >>> a1 = Account('Brian')
    >>> a1.deposit(100)
    100
    >>> a2 = Account('Brian')
    >>> Account.deposit(a2, 100)
    100

    >>> a = Account('Brian')
    >>> a.deposit(100)
    100
    >>> a.balance
    100
    >>> hasattr(a, 'balance')
    True
    >>> hasattr(a, 'ecnalab')
    False
    >>> getattr(a, 'balance')  # same as a.balance
    100
    >>> getattr(a, 'deposit')(100)
    200

    >>> type(Account.deposit)
    <class 'function'>
    >>> type(a.deposit)
    <class 'method'>

    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    >>> a.interest = 0.06
    >>> a.interest
    0.06
    """

    interest = 0.02  # A class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals.

    >>> ch = CheckingAccount('Marvin')
    >>> ch.interest
    0.01
    >>> ch.deposit(20)
    20
    >>> ch.withdraw(5)
    14
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
