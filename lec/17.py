"""Mutable Linked Lists"""

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        if not (rest is Link.empty or isinstance(rest, Link)):
            raise ValueError('rest must be Link or empty')
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(
                self.first)
        else:
            return 'Link({}, {})'.format(
                self.first, repr(self.rest))

    def __len__(self):
        return 1 + len(self.rest)  # Where's the base case??

    def __getitem__(self, i):
        if i == 0:
            return self.first
        elif self.rest is Link.empty:
            raise IndexError('linked list index out of range')
        else:
            # return self.rest.__getitem__(i-1)
            return self.rest[i-1]

    def __setitem__(self, i, val):
        if i == 0:
            self.first = val
        elif self.rest is Link.empty:
            raise IndexError('linked list assignment index out of range')
        else:
            self.rest[i-1] = val

    def map(self, f):
        # for i in range(len(self)):
        #     self[i] = f(self[i])
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)

    def contains(self, e):
        if self.first == e:
            return True
        elif self.rest is Link.empty:
            return False
        else:
            return self.rest.contains(e)

    def __contains__(self, e):
        # if self.first == e:
        #     return True
        # else:
        #     return e in self.rest
        return self.first == e or e in self.rest

    def insert_front(self, e):
        self.rest = Link(self.first, self.rest)
        self.first = e

    def remove_front(self):
        self.first = self.rest.first
        self.rest = self.rest.rest

def mutate_example():
    """
    >>> link = Link(1, Link(2))
    >>> link
    Link(1, Link(2))
    >>> link.first = 4
    >>> link
    Link(4, Link(2))

    >>> link = Link('I', Link('love', Link('cs61a')))
    >>> link
    Link(I, Link(love, Link(cs61a)))
    >>> link.rest.rest.first = 'POKÉMON'
    >>> link 
    Link(I, Link(love, Link(POKÉMON)))
    >>> link.rest = Link('really', link.rest)
    >>> link.rest = Link('really', link.rest)
    >>> link.rest = Link('really', link.rest)
    >>> link
    Link(I, Link(really, Link(really, Link(really, Link(love, Link(POKÉMON))))))
    """


class Frame(Link):
    """An environment is a sequence of Frames. An environment frame binds names
    to values.

    >>> Frame.number = 0
    >>> g = Frame('Global')
    >>> g.define('x', 2)
    >>> g.lookup('x')
    2

    >>> f1 = Frame('func1', g)
    >>> f2 = Frame('func2', f1)
    >>> f2.lookup('x')
    2

    >>> f1.define('x', 3)
    >>> f2.lookup('x')
    3
    >>> f3 = Frame('func2', f1)
    >>> f3.lookup('x')
    3

    >>> f1.define('x', 4)
    >>> f3.lookup('x')
    4

    >>> print(f3)
    <f3: func2 [parent=f1]>
    """

    empty = ()
    number = 0

    def __init__(self, name, parent=empty):
        Link.__init__(self, {}, parent)
        self.name = name

        self.number = Frame.number
        Frame.number += 1

    @property
    def bindings(self):
        return self.first

    @property
    def parent(self):
        return self.rest

    def __repr__(self):
        if self.parent is Frame.empty:
            return 'Frame({}, {})'.format(self.name, self.bindings)
        else:
            return 'Frame({}, {}, {})'.format(self.name, self.bindings, repr(self.parent))


    def __str__(self):
        if self.parent is Frame.empty:
            return '<Global>'
        else:
            return '<f{0}: {1} [parent=f{2}]>'.format(self.number,
                                                      self.name,
                                                      self.parent.number)


    def define(self, name, value):
        self.bindings[name] = value

    def lookup(self, name):
        if name in self.bindings:
            return self.bindings[name]
        elif self.parent is Frame.empty:
            raise NameError("name '{}' is not defined".format(name))
        else:
            return self.parent.lookup(name)


from functools import wraps
import inspect
Frame.number = 0
global_frame = Frame('Global')
call_stack = Link(global_frame)

def brython(fn):
    # A function's parent frame is the current frame when it is defined
    parent_frame = call_stack.first

    # Python magic to determine a function's name and parameters
    fn_name = fn.__name__
    params = inspect.getargspec(fn).args

    @wraps(fn)  # Stops decorated functions from looking like "br_func"
    def br_func(*args):
        # When a function is called, a new call frame is created
        # and added to the top of the stack
        call_frame = Frame(fn_name, parent_frame)
        call_stack.insert_front(call_frame)
        print(call_stack)

        # Bind parameters to arguments in the call frame
        for param, arg in zip(params, args):
            call_frame.define(param, arg)

        # Call function with the arguments
        result = fn(*args)

        # After the function returns, it is removed from the stack
        call_stack.remove_front()
        return result

    # Bind the function's name to the function in the parent frame
    parent_frame.define(fn_name, br_func)
    return br_func

@brython
def square(x):
    # return x * x

    frame = call_stack.first
    return frame.lookup('x') * frame.lookup('x')

@brython
def factorial(n):
    # if n == 0:
    #     return 1
    # else:
    #     return n * factorial(n-1)

    frame = call_stack.first
    if frame.lookup('n') == 0:
        return 1
    else:
        return frame.lookup('n') * frame.lookup('factorial')(frame.lookup('n') - 1)

@brython
def fib(n):
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return fib(n-1) + fib(n-2)

    frame = call_stack.first
    if frame.lookup('n') == 0:
        return 1
    elif frame.lookup('n') == 1:
        return 1
    else:
        return frame.lookup('fib')(frame.lookup('n') - 1) + \
            frame.lookup('fib')(frame.lookup('n') - 2)

@brython
def make_adder(n):
    @brython
    def adder(k):
        # return n + k

        frame = call_stack.first
        return frame.lookup('n') + frame.lookup('k')

    # return adder
    frame = call_stack.first
    return frame.lookup('adder')
