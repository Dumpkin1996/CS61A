# Approximation

5 / 3
5 // 3
5 % 3


# Multiple return values

def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(2016, 10)


# Docstrings, doctests, & default arguments

def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing n by d.

    >>> quotient, remainder = divide_exact(2016, 10)
    >>> quotient
    201
    >>> remainder
    6
    >>> quotient, remainder = divide_exact(2016)
    >>> quotient
    201
    >>> remainder
    6
    """
    return n // d, n % d


# Lambda expressions

x = 10
square = x * x
square = lambda x: x * x
square(4)
(lambda x: x * x)(4)
