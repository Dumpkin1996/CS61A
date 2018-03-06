# Generators

# Q1

def permutations(lst):
    """Generates all permutations of sequence LST.  Each permutation is a
    list of the elements in LST in a different order.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    if not lst:
        yield []
        return 
    else:
    	previous = sorted(permutations(lst[1:]))
    	for previous_lst in previous:
    		for i in range(len(lst)):
    			yield previous_lst[:i] + [lst[0]] + previous_lst[i:]		
# Review

# Q2

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    if x > power_of_two:
    	while power_of_two < x:
    		power_of_two *= 2
    	candidate1 = power_of_two
    	candidate2 = power_of_two//2
    	if candidate1 - x <= x - candidate2:
    		return candidate1
    	else:
    		return candidate2
    else:
    	while power_of_two > x:
    		power_of_two *= 0.5
    	candidate1 = power_of_two*2
    	candidate2 = power_of_two
    	if candidate1 - x <= x - candidate2:
    		return candidate1
    	else:
    		return candidate2	

# Q3

def repeated(f, n):
    """Returns a single-argument function that takes a value, x, and applies
    the single-argument function F to x N times.
    >>> repeated(lambda x: x*x, 3)(2)
    256
    """
    def h(x):
        for k in range(n):
            x = f(x)
        return x
    return h

def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    smooth_dx = lambda f: smooth(f, dx)
    return repeated(smooth_dx, n)(f)

# Q4

def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_count = 0
    def make_counter():
    	count = 0
    	def counter(input):
    		nonlocal count, global_count
    		if input == 'count':
    			count += 1
    			return count
    		if input == 'global-count':
    			global_count += 1
    			return global_count
    		if input == 'reset':
    			count = 0
    		if input == 'global-reset':
    			global_count = 0
    	return counter
    return make_counter

# Q5

def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    return [[suit, rank] for suit in suits for rank in ranks]

# Q6

def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    return [deck[k//2] if k%2==0 else deck[(len(deck)+k-1)//2] for k in range(len(deck))]
# Q7

def is_circular(G):
    """Return true iff G represents a circular directed graph."""
    for v in G:
        if reaches_circularity(G, v):
            return True
    return False

def reaches_circularity(G, v0):
    """Returns true if there is a circularity in G in some path
    starting from vertex V0.
    >>> G = { 'A': ['B', 'D'], 'B': ['C'], 'C': ['F'], 'D': ['E'], 
    ...       'E': ['F'], 'F': ['G'], 'G': ['A'] }
    >>> is_circular(G)
    True
    >>> G['F'] = []
    >>> is_circular(G)
    False
    """
    current_path = []
    def is_path_to_cycle(v1):
        nonlocal current_path
        current_path += [v1]
        for w in G[v1]:
            if w in current_path:
                return True
            if is_path_to_cycle(w):
                return True
        current_path.remove(v1)
        return False
    return is_path_to_cycle(v0)    

# Q8

class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1+len(self.rest)

def intersection(xs, ys):
    """
    >>> a = Link(1)
    >>> intersection(a, Link.empty) is Link.empty
    True

    >>> b = a
    >>> intersection(a, b).first # intersection begins at a
    1

    >>> looks_like_a = Link(1)
    >>> intersection(a, looks_like_a) is Link.empty # no intersection! (identity vs value)
    True

    >>> b = Link(1, Link(2, Link(3, a)))
    >>> a.first = 5
    >>> intersection(a, b).first # intersection begins at a
    5

    >>> c = Link(3, b)
    >>> intersection(b, c).first # intersection begins at b
    1
    >>> intersection(c, b).first # intersection begins at b
    1

    >>> intersection(a, c).first # intersection begins at a
    5
    """
    if xs == ys:
        return xs
    elif len(xs) > len(ys):
        return intersection(xs.rest, ys)
    elif len(xs) < len(ys):
        return intersection(xs, ys.rest)
    elif len(xs) == len(ys):
        return intersection(xs.rest, ys.rest)