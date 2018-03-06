from lab03 import *

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0 or n == 1:
        return n
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        print (i)
        if i < n:
            counter(i+1)
    counter(1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a > b:
        return gcd(b, a)
    else:
        if b%a == 0:
            return a
        else:
            return gcd (a,b%a)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b == 0:
        return c
    else:
        return ab_plus_c(a, b-1, c)+a

def has_sublist(l, sublist):
    """Returns whether the elements of sublist appear in order anywhere within list l.
    >>> has_sublist([], [])
    True
    >>> has_sublist([3, 3, 2, 1], [])
    True
    >>> has_sublist([], [3, 3, 2, 1])
    False
    >>> has_sublist([3, 3, 2, 1], [3, 2, 1])
    True
    >>> has_sublist([3, 2, 1], [3, 2, 1])
    True
    """
    if len(sublist) == 0:
        return True
    else:
        if len(sublist) >= len(l):
            return True if sublist == l else False
        else:
            return has_sublist(l[1:], sublist) or has_sublist(l[:-1], sublist)

def remove_first(lst, elem):
    """ This function removes the first appearance of elem in list lst.

    >>> remove_first([3, 4] , 3)
    [4]
    >>> remove_first([3, 4, 3] , 3)
    [4, 3]
    >>> remove_first([2, 4] , 3)
    [2, 4]
    >>> remove_first([] , 0)
    []
    """
    if lst == []:
        return lst
    if lst[0] == elem:
        return lst[1:]
    else:
        return lst[:1] + remove_first(lst[1:], elem)

def sort(lst):
    """This function returns a sorted version of the list lst.

    >>> sort([6, 2, 5])
    [2, 5, 6]
    >>> sort([2, 3])
    [2, 3]
    >>> sort([3])
    [3]
    >>> sort([])
    []
    """ 
    if lst == []:
        return lst
    else:
        x = min(lst)
        return [x] + sort(remove_first(lst, x))

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def interleaved_sum_helper (current_term, the_other_term, x):
        if x == n:
            return current_term(n)
        else:
            return current_term(x) + interleaved_sum_helper(the_other_term, current_term, x + 1)
    return interleaved_sum_helper (odd_term, even_term, 1)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count(x, m = n):
        if m%10 == m:
            if x == m:
                return 1
            else:
                return 0
        elif m%10 == x:
            return count(x, m//10) + 1
        else:
            return count(x, m//10)
    return count(1)*count(9) + count(2)*count(8) + count(3)*count(7) + count(4)*count(6) + (count(5)*(count(5)-1))//2

def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n == 1:
        return False
    else:
        def check_factor(x):
            if x == n:
                return True
            elif n%x == 0:
                return False
            else:
                return check_factor(x+1)
        return check_factor(2)
