from functools import reduce
from operator import add, sub, mul, truediv


# Constants

SYMBOLS = {'(', ')', '+', '-', '*', '/'}

def calc_add(*args):
    return reduce(add, args, 0)

def calc_sub(*args):
    if len(args) == 0:
        raise TypeError('not enough arguments to -')
    if len(args) == 1:
        return -args[0]
    return reduce(sub, args[1:], args[0])

def calc_mul(*args):
    return reduce(mul, args, 1)

def calc_div(*args):
    if len(args) == 0:
        raise TypeError('not enough arguments to /')
    if len(args) == 1:
        return 1 / args[0]
    return reduce(truediv, args[1:], args[0])

OPERATORS = {'+': calc_add, '-': calc_sub,
             '*': calc_mul, '/': calc_div}


# The Pair class

class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return 'Pair({}, {})'.format(repr(self.first), repr(self.second))

    def __str__(self):
        result = '(' + str(self.first)
        while isinstance(self.second, Pair):
            self = self.second
            result += ' ' + str(self.first)
        if self.second is nil:
            return result + ')'
        return result + ' . ' + str(self.second) + ')'

    def __len__(self):
        return 1 + len(self.second)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.second[i-1]

    def map(self, fn):
        return Pair(fn(self.first), self.second.map(fn))

class nil:
    """Represents the special empty pair nil in Scheme."""
    def __repr__(self):
        return 'nil'

    def __str__(self):
        return '()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('Index out of range')

    def map(self, fn):
        return nil

nil = nil()


# Parsing: Lexical Analysis

def tokenize(string):
    """Splits the provided string into a list of tokens."""
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')
    tokens = string.split()
    if tokens.count('(') != tokens.count(')'):
        raise SyntaxError('unbalanced parentheses')
    for i in range(len(tokens)):
        token = tokens[i]
        if token not in SYMBOLS:
            to_num = numberize(token)
            if to_num == None:
                raise SyntaxError('unexpected token: ' + str(token))
            tokens[i] = to_num
    return tokens

def numberize(exp):
    """Converts exp to a number if possible, otherwise returns None."""
    try:
        return int(exp)
    except ValueError:
        try:
            return float(exp)
        except ValueError:
            return None


# Parsing: Syntactic Analysis

def read_exp(tokens):
    """Given a list of tokens, returns the first calculator expression
    (either a number, operator, or Pair).
    """
    token = tokens.pop(0)
    if token == '(':  # Start of a Pair
        exp = read_tail(tokens)
        if exp is nil:
            raise TypeError('nil is not a valid expression')
        return exp
    elif token == ')':  # End of a Pair?
        raise SyntaxError('unexpected )')
    else:  # operator or number
        return token

def read_tail(tokens):
    """Reads up to and including the first mismatched close parenthesis,
    then forms a combination out all of the values read up to that point.
    """
    if tokens[0] == ')':  # Finished
        tokens.pop(0)
        return nil
    return Pair(read_exp(tokens), read_tail(tokens))


# Evaluation

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair."""
    if isinstance(exp, Pair):
        op = calc_eval(exp.first)
        args = list(exp.second.map(calc_eval))
        return calc_apply(op, args)
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:  # Just a number
        return exp

def calc_apply(op, args):
    """Applies an operator to a Pair of arguments."""
    return op(*args)


# Read-Eval-Print Loop

def repl():
    """The main read-eval-print loop for the Calculator language."""
    while True:
        try:
            text = get_input()
            exp = read_exp(tokenize(text))
            print(calc_eval(exp))
        except (SyntaxError, TypeError, ZeroDivisionError) as e:
            print(type(e).__name__ + ':', e)
        except (KeyboardInterrupt, EOFError):
            print('\nCalculation complete.')
            return

def get_input():
    """Asks for input while there are fewer open than close parens."""
    line = input('calc> ')
    while line.count('(') > line.count(')'):
        line += ' ' + input('      ')
    return line

repl()
