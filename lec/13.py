"""Mutable Functions"""

# Nonlocal Assignment

def make_withdraw(balance):
    """Return a withdraw function with a starting balance.

    >>> w = make_withdraw(100)
    >>> w(10)
    90
    >>> w(10)
    80
    >>> w(10)
    70
    >>> w(20)
    50
    >>> w(10000)
    'Insufficient funds'
    >>> w(10)
    40
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

# Mutable Sequences

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

# Multiple Mutable Functions

brian = make_withdraw(100)
marvin = make_withdraw(100000)
brian is not marvin
brian != marvin
brian(10)
brian(10)
marvin(1000)
brian(10)
marvin(1000)
brian(1000)
marvin(97930)

# Referential Transparency

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
b(3) + b(4)

# Mutating Linked Lists

empty = 'X'

def link(first, rest=empty):
    def dispatch(m, *args):
        nonlocal first
        if m == 'first':
            return first
        elif m == 'rest':
            return rest
        elif m == 'set':
            i, v = args
            if i == 0:
                first = v
            else:
                setitem(rest, i-1, v)
    return dispatch

def first(lnk):
    return lnk('first')

def rest(lnk):
    return lnk('rest')

def print_link(lnk):
    """Prints out a non-deep linked list."""
    line = ''
    while lnk != empty:
        if line:
            line += ' '
        line += str(first(lnk))
        lnk = rest(lnk)
    print('<{}>'.format(line))


def setitem(lnk, i, v):
    """Sets the element at index i to v.

    >>> lnk = link(1, link(2, link(3, empty)))
    >>> print_link(lnk)
    <1 2 3>
    >>> setitem(lnk, 0, 4)
    >>> print_link(lnk)
    <4 2 3>
    >>> setitem(lnk, 1, 5)
    >>> print_link(lnk)
    <4 5 3>
    >>> setitem(lnk, 2, 6)
    >>> print_link(lnk)
    <4 5 6>
    """
    lnk('set', i, v)
