HW_SOURCE_FILE = 'hw03.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    result1, result2, result3 = 1, 2, 3
    for i in range (n-3):
        result1 = 3*result1 + 2*result2 + result3
        result1, result2, result3 = result2, result3, result1
    if n == 1:
        return result1
    elif n == 2:
        return result2
    else:
        return result3

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def pingpong_helper(x, current, opposite):
        if x == n:
            return current(n-1)
        elif x%7 == 0 or has_seven(x):
            return pingpong_helper(x+1, opposite, current) + current(x)
        else:
            return pingpong_helper(x+1, current, opposite) + current(x)
    return pingpong_helper (1, lambda x: 1, lambda x: -1)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    x = amount//2
    def count_change_helper(amount, largest):
        if amount < 0:
            return 0
        elif largest == 1:
            return 1
        else:
            def sum(amount, largest):
                result = 0
                for i in range(0,x+1):
                    result += count_change_helper(amount-i*largest, largest//2)
                return result
            return sum(amount, largest)
    y = 1
    while y < amount:
        y *= 2
    return count_change_helper(amount, y//2)

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    transition = 6 - start - end
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, transition)
        print_move(start, end)
        move_stack(n-1, transition, end)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    if len(lst) == 1:
        if type(lst[0]) != list:
            return lst
        else:
            return flatten(lst[0])
    if type(lst[0]) != list:
        return lst[0:1] + flatten(lst[1:])
    else:
        return flatten(lst[0]) + flatten(lst[1:])

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    if lst1[0] <= lst2[0]:
        return lst1[0:1] + merge(lst1[1:], lst2)
    elif lst2[0] < lst1[0]:
        return lst2[0:1] + merge(lst1, lst2[1:])

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    a = len(seq)
    if a == 1 or a == 0:
        return seq
    if a == 2:
        return [min(seq)] + [max(seq)]
    else:
        return merge (mergesort(seq[0:a//2]), mergesort(seq[a//2: a]))

###################
# Extra Questions #
###################

from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    return Y(lambda h: lambda n: 1 if n==1 or n==0 else n*h()(n-1))  # Replace 
