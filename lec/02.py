# Names
x = 1
y = x + x
x, y = y, x + y


# Environment Diagrams
x = 1
y = x
x = 2


# User-defined Functions
def square(x):
    return x * x
y = square(-2)


# Multiple Environments
y = square(square(-2))


# None
def does_not_square(x):
    x * x
not_four = does_not_square(-2)
# not_four + 4 # Error!


# Nested Print Expressions
print(print(1), print(2))


# More Functions
def describe(f, x):
    """
    >>> four = describe(square, -2)
    Calling function with argument -2
    Result was 4
    >>> four
    4
    >>> sixteen = describe(square, four)
    Calling function with argument 4
    Result was 16
    >>> sixteen
    16
    """
    print('Calling function with argument', x)
    result = f(x)
    print('Result was', result)
    return result
