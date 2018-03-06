# List comprehensions

odds = [1, 3, 5, 7, 9]
[x + 1 for x in odds]
[x for x in odds if 25 % x == 0]
n = 3
[abs(n) for n in range(4, 8) if n % 2 == 0]


# Division loses exact representation of fractions

103/191 * 191/103

# So instead of floating point numbers, we want something like:
# >>> x = rational(103, 191)
# >>> numer(x)
# 103
# >>> denom(x)
# 191


# Rational arithmetic

def mul_rational(rat1, rat2):
    """Multiply the rational numbers rat1 and rat2 and return a new
    rational number.
    """
    return rational(numer(rat1) * numer(rat2), denom(rat1) * denom(rat2))

def add_rational(rat1, rat2):
    """Add the rational numbers rat1 and rat2 and return a new rational
    number.
    """
    n1, d1 = numer(rat1), denom(rat1)
    n2, d2 = numer(rat2), denom(rat2)
    return rational(n1 * d2 + n2 * d1, d1 * d2)

def rationals_are_equal(rat1, rat2):
    """Return whether the rational numbers rat1 and rat2 are equal."""
    return numer(rat1) * denom(rat2) == numer(rat2) * denom(rat1)

def print_rational(rat):
    """Print the rational number rat."""
    print(numer(rat), '/', denom(rat))


# Rational number constructor and selectors

from fractions import gcd  # Greatest common divisor
def rational(n, d):
    """Return the rational number with numerator n and denominator d,
    in lowest terms.
    """
    divisor = gcd(n, d)  # Reduce to lowest terms
    return [n//divisor, d//divisor]
    # Alternate implementation:
    # return {'n': n//divisor, 'd': d//divisor}

def numer(rat):
    """Return the numerator of the rational number rat."""
    return rat[0]
    # Alternate implementation:
    # return rat['n']

def denom(rat):
    """Return the denominator of the rational number rat."""
    return rat[1]
    # Alternate implementation:
    # return rat['d']


# Python Dictionaries

d = {'a': 1, 'b': True, 'c': [1, 2, 3], 4: 'hello'}
d['a']
# d['hello']  # Gives a KeyError
d['a'] = 3
d['hello'] = 45

for elem in d.keys():  # Iterates through keys
    print(elem)
# Note: For convenience, Python also lets you do `for elem in d:` to
#       iterate through keys

for elem in d.values():  # Iterates through values
    print(elem)

for key, value in d.items():  # Iterates through keys and values
    print(key, 'has value:', value)

# The above is an example of multiple assignment, e.g., we can do:
for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(a, b)


# Dictionary ADT

# We will have one constructor `dictionary(keys, values)`,
# and three selectors:
#     `get_val(dict, key)` Returns the value associated with key in dict
#         or prints an error if key is not in dict.
#     `put_val(dict, key, val)` Returns a new dictionary that is the
#         same as dict, but with val associated with key. This either
#         creates a new association or overwrites an existing one, if
#         key was already in dict.
#     `get_all_keys(dict)` Returns a list of all keys in dict.
# Let's not write this code yet, so we don't break abstraction barriers

def get_values(dict):
    """Returns a list of all values in the dictionary dict."""
    return [get_val(dict, key) for key in get_all_keys(dict)]

def get_items(dict):
    """Returns a list of two-element tuples, where the first element is
    a key in dict and the second element is the corresponding value.
    """
    keys, values = get_all_keys(dict), get_values(dict)
    return [(keys[i], values[i]) for i in range(len(keys))]


# Dictionary constructors and selectors

def dictionary(keys, values):
    if len(keys) != len(values):
        print('Error: keys and values have different lengths!')
    return (keys, values)

def get_val(dict, key):
    keys, vals = dict
    # Go backwards to find newest value, in case a key was overwritten
    i = len(keys) - 1  # Last index
    while i >= 0:
        if keys[i] == key:
            return vals[i]
        i -= 1
    print('Error: key', key, 'not found!')

def put_val(dict, key, val):
    return (dict[0] + [key], dict[1] + [val])

def get_all_keys(dict):
    return list(set(dict[0]))  # Remove duplicates, then convert back


# Using our dictionary ADT

my_dict = dictionary(['a', 'b', 'c', 4], [1, True, [1, 2, 3], 'hello'])
get_val(my_dict, 'a')
get_val(my_dict, 'hello')
my_dict = put_val(my_dict, 'a', 3)  # Returns a new updated dictionary
my_dict = put_val(my_dict, 'hello', 45)

for elem in get_all_keys(my_dict):
    print(elem)
# We can't implement `for elem in my_dict:` for convenience :/ Yet...

for elem in get_values(my_dict):
    print(elem)

for key, value in get_items(my_dict):
    print(key, 'has value:', value)
