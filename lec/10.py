"""Sequences and Linked Lists"""

# Sequences

odds = [41, 43, 45, 47, 49, 51, 53]
len(odds)
odds[1]
odds[0] * odds[4] + len(odds)
odds[odds[3]-odds[2]]

fun = 'cs61a'
len(fun)
fun[0]

from operator import getitem
getitem(odds, 0) * getitem(odds, 4) + len(odds)

# Linked Lists

empty = 'X'

def link(first, rest):
    return [first, rest]

def first(s):
    assert s != empty, 'empty linked list has no first'
    return s[0]

def rest(s):
    assert s != empty, 'empty linked list has no rest'
    return s[1]

four = link(1, link(2, link(3, link(4, empty))))
march = link(1, link(2, link(1, link(2, empty))))
v1 = link(march, four)
v2 = link(march, link(four, empty))
first(rest(rest(rest(v1))))

# Which of these evaluates to 3?
# first(rest(rest(first(rest(v2)))))
# first(rest(first(rest(rest(v2)))))
# first(rest(first(rest(first(v2)))))
# first(rest(rest(rest(first(v2)))))
# first(first(rest(rest(first(v2)))))


# Linked Lists are Sequences

def len_link(s):
    """Return the length of the linked
    list.

    >>> len_link(four)
    4
    >>> len_link(v2)
    2
    """
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i.

    >>> getitem_link(march, 3)
    2
    """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


# Linked Lists are Recursive

def len_link_recursive(s):
    """Return the length of the linked
    list."""
    if s == empty:
        return 0
    else:
        return 1 + len_link_recursive(rest(s))

def getitem_link_recursive(s, i):
    """Return the element at index i."""
    if i == 0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s), i - 1)


# Sequences as Containers

def contains(s, elem):
    """Return whether ELEM is in the
    sequence S.

    >>> contains([1, 2, 3], 1)
    True
    >>> contains([1, 2, 3], 4)
    False
    """
    for x in s:
        if x == elem:
            return True
    return False

def contains_link(s, elem):
    """Return whether ELEM is in the linked list S.

    >>> contains_link(four, 1)
    True
    >>> contains_link(four, 5)
    False
    """
    if s == empty:
        return False
    if first(s) == elem:
        return True
    else:
        return contains_link(rest(s), elem)


# Linked List Examples

def join_link(s, separator):
    """Return a string of all elements
    in S separated by SEPARATOR.

    >>> join_link(four, ', ')
    '1, 2, 3, 4'
    """
    if s == empty:
        return ''
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

def print_link(s):
    print('<' + join_link(s, ' ') + '>')
        
def extend_link(s, t):
    """Return a list with the elements
    of S followed by those of T.

    >>> s = extend_link(four, four)
    >>> print_link(s)
    <1 2 3 4 1 2 3 4>
    """
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def reverse_link(s):
    """Return S reversed.

    >>> s = reverse_link(four)
    >>> print_link(s)
    <4 3 2 1>
    """
    return reverse_to(s, empty)

def reverse_to(s, reversed):
    """
    >>> s = reverse_to(link(3, link(4, empty)),
    ...                link(2, link(1, empty)))
    >>> print_link(s)
    <4 3 2 1>
    """
    if s == empty:
        return reversed
    else:
        return reverse_to(rest(s), link(first(s), reversed))

def map_link(f, s):
    """Apply F to each element of S.

    >>> s = map_link(lambda x: x * x, four)
    >>> print_link(s)
    <1 4 9 16>
    """
    if s == empty:
        return s
    else:
        return link(f(first(s)),
                    map_link(f, rest(s)))

def partitions(n, m):
    """Return a linked list of
    partitions of n using parts of up to
    m. Each partition is represented as
    a linked list.

    >>> s = partitions(6, 4)
    >>> len_link(s)
    9
    """
    if n == 0:
        return link(empty, empty)  # a list containing the empty partition
    elif n < 0:
        return empty
    elif m == 0:
        return empty
    else:
        used_m = partitions(n - m, m)
        add_m = lambda s: link(m, s)
        with_m = map_link(add_m, used_m)
        without_m = partitions(n, m - 1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    """Print the partitions of n using
    parts of up to m.

    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, ' + '), lists)
    print(join_link(strings, '\n'))


# Other Linked List Implementations

def link(first, rest):
    def dispatch(msg):
        if msg == 'first':
            return first
        elif msg == 'rest':
            return rest
    return dispatch

def first(s):
    return s('first')

def rest(s):
    return s('rest')
