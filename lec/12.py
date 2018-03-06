# Dictionary ADT from Lecture 9

def get_values(dict):
    """Returns a list of all values in the dictionary dict."""
    values = []
    keys = get_all_keys(dict)
    for key in keys:
        values += [get_val(dict, key)]
    return values

def get_items(dict):
    """Returns a list of two-element tuples, where the first element is
    a key in dict and the second element is the corresponding value.
    """
    items = []
    keys, values = get_all_keys(dict), get_values(dict)
    for i in range(len(keys)):
        items += [(keys[i], values[i])]
    return items


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
    # Mutable ADT:
    # dict[0].append(key)
    # dict[1].append(val)
    return (dict[0] + [key], dict[1] + [val])

def get_all_keys(dict):
    return list(set(dict[0]))  # Remove duplicates, then convert back


# Speed test

from time import time

d = {}  # Built-in: `d = {}`, ADT: `d = dictionary([], [])`
now = time()
total_time = 0

for i in range(1, 100001):
    # Built-in: `d[i] = i`
    # Immutable ADT: `d = put_val(d, i, i)`, Mutable: `put_val(d, i, i)`
    d[i] = i
    if i % 10000 == 0:
        delta = time() - now
        print('Adding numbers', i - 9999, 'to', i, 'took', delta, 'seconds.')
        total_time += delta
        now = time()
total_time += time() - now


# Lists

suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']


# Python Dictionaries

numerals = {'I': 1.0, 'V': 5, 'X': 10}
numerals['X']
numerals['I'] = 1
numerals['L'] = 50
sum(numerals.values())


# Sets

bills = {1, 2, 5, 10}
bills.add(20)
big_bills = set(['Grant', 'Franklin'])
bills.update(big_bills)
bills.remove(2)
5 in bills
bills.pop()


# Group by keys

def group_by_key(pairs):
    """Return a dictionary that maps unique keys to corresponding values
    from a list of [key, value] pairs

    >>> example = [[1, 2], [3, 2], [1, 3], [3, 1], [1, 2]]
    >>> group_by_key(example)
    {1: [2, 3, 2], 3: [2, 1]}
    """
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)
    return d


# Tuples are immutable

tup = (3, 4, 5, 6)
one = (2,)
two = (3,) + tuple([5])
5 in tup
len(tup)
# tup[2] = 0
w, x, y, z = tup
valid = {(1, 2): 3}
# invalid = {[1, 2]: 3}
# invalid = {([1], 2): 3}


# Strings are also immutable

string = 'ABC'
# string[2] = 'e'
len('apple')
'banana'[:2]
words = 'This is a sentence.'.split()
' '.join(words)


# Identity vs Equality

a = [10]
b = [10]
a == b
a.extend([20, 30])
a == b
c = b
c == b
c.pop()
c == b
