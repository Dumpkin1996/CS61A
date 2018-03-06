# Recursive factorial

def factorial(n):
    """Return the factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Sum digits

def sum_digits(n):
    """Return the sum of the digits of positive integer n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        return sum_digits(n//10) + n%10


# Iterative factorial
# Key idea in converting recursion to iteration: try to make the state
# maintained in each iteration the same as the state maintained by each
# recursive call

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


# Converting back to recursion
# More formulaic: whatever state is maintained in each iteration, pass
# that in as arguments to the recursive function

def fact2(n, total):
    if n == 0:
        return total
    else:
        return fact2(n-1, total*n)

# Can be ugly or complicated, but often not too hard to clean up

fact = lambda n: fact2(n, 1)


# Minimum element in list

def minimum(lst):
    """Return the minimum element in lst, a nonempty list of numbers.

    >>> minimum([0])
    0
    >>> minimum([1, 2, 3])
    1
    >>> minimum([1, -1, -4000, 2, 170])
    -4000
    """
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], minimum(lst[1:]))


# Reverse string

def reverse(word):
    """Given the string word, return word in reverse.

    >>> reverse('')
    ''
    >>> reverse('a')
    'a'
    >>> reverse('Hello world!')
    '!dlrow olleH'
    """
    if len(word) < 2:
        return word
    else:
        return reverse(word[1:]) + word[0]
