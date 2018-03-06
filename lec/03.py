# Conditional expressions

def absolute_value(x):
    """Return the absolute value of x.

    >>> absolute_value(-3)
    3
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    else:
        return x

def sgn(x):
    """Return the sign of x, which is -1 if x is negative, 0 if x is 0,
    and 1 if x is positive.

    >>> sgn(-3)
    -1
    >>> sgn(0)
    0
    >>> sgn(3)
    1
    """
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


# Boolean expressions

not 1
not 0
False and True
True or False
# 1/0  # gives an error
0 and 1/0
# 0 or 1/0  # gives an error
1 and 2 and 3 and 'Hi!'


# Iteration

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    i, total = 1, 1
    while i < n:
        i += 1
        total *= i
    return total


# Sequences

l = [1, 2, 3, 4]
l[2]  # All sequences support indexing
l[-2]
l[1:3]  # and slicing
t = (1, 2, 3, 4)
r = range(1, 5)
# Strings are sequences of characters, which are also themselves strings
s = 'Hello world!'
# Dictionaries aren't sequences, but are very useful nonetheless
d = {'a': 1, 'b': 2, 'c': 3}
d['a']  # Dictionaries can be indexed, but not sliced

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


# List of factors

def factors_list(n):
    """Return a list containing all the numbers that divide n evenly,
    except for the number itself.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    x = 1
    while x < n:
        if n % x == 0:
            all_factors += [x]
        x += 1
    return all_factors
