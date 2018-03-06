# Generators

def range_gen(start, end):
    """Returns a generator that iterates from start to end - 1.

    >>> for i in range_gen(0, 5):
    ...     print(i)
    ... 
    0
    1
    2
    3
    4
    """
    while start < end:
        yield start
        start += 1

def naturals():
    """Returns a generator that iterates over the natural numbers.

    >>> n = naturals()
    >>> next(n)  # Equivalent to n.__next__()
    0
    >>> next(n)
    1
    """
    curr = 0
    while True:
        yield curr
        curr += 1


# Iterating over binary search trees

class BST:
    empty = ()
    def __init__(self, entry, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.entry = entry
        self.left, self.right = left, right

        if left is not BST.empty: 
            assert left.max <= entry
        if right is not BST.empty: 
            assert entry < right.min
            
    @property
    def max(self): # Returns the maximum element in the tree
        if self.right is BST.empty:
            return self.entry
        return self.right.max

    @property
    def min(self): # Returns the minimum element in the tree
        if self.left is BST.empty:
            return self.entry
        return self.left.min

    def __iter__(self):
        """Iterates over the elements of the BST in order.
        An equivalent alternate implementation:

        for elem in self.left:
            yield elem
        yield self.entry
        for elem in self.right:
            yield elem
        """
        yield from self.left
        yield self.entry
        yield from self.right


# Coroutines

def match(pattern):
    """Receives and prints input that contains a pattern.

    >>> matcher = match('hello')
    >>> next(matcher)
    Looking for hello
    >>> matcher.send('hello there')
    hello there
    >>> matcher.send('goodbye now')
    >>> matcher.send('Othello is a great play')
    Othello is a great play
    >>> matcher.close()
    Done.
    """
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                print(s)
    except GeneratorExit:
        print('Done.')


# Sequence processing

def coroutine(func):
    """Decorator that automatically preps coroutines for us."""
    def call_next_once(*args):
        cr = func(*args)
        next(cr)
        return cr
    return call_next_once

def producer(next_coroutines):
    """Accepts user input and sends it to next_coroutines."""
    try:
        while True:
            s = input('Send me data: ')
            for cr in next_coroutines:
                cr.send(s)
    except KeyboardInterrupt:
        for cr in next_coroutines:
            cr.close()

@coroutine
def filter(next_coroutines, pred, map):
    """Receives input and sends the result of calling map on the input to
    next_coroutines if the input satisfies pred.
    """
    try:
        while True:
            s = (yield)
            if pred(s):
                for cr in next_coroutines:
                    cr.send(map(s))
    except GeneratorExit:
        for cr in next_coroutines:
            cr.close()

@coroutine
def consumer():
    """Receives input and prints it."""
    print('Ready to print')
    try:
        while True:
            s = (yield)
            print(s)
    except GeneratorExit:
        print('Done.')


true = lambda s: True
identity = lambda s: s

printer = consumer()
matcher = filter([printer], lambda s: 'MARVIN' in s, identity)
matcher2 = filter([printer], lambda s: 'BRIAN' in s, identity)
caps = filter([matcher, matcher2], true, lambda s: s.upper())

# To start the pipeline:
producer([caps])
