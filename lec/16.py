# ElectricType inheritance example

class Pokemon:
    """A Pokemon class.

    >>> squirt = Pokemon('Squirtle', 'Marvin')
    >>> squirt.trainer
    'Marvin'
    >>> squirt.speak()
    Squirtle!
    >>> bulba = Pokemon('Bulbasaur', 'Brian')
    >>> bulba.hp
    50
    >>> squirt.attack(bulba)
    Squirtle!
    Squirtle used tackle on Bulbasaur!
    >>> bulba.hp
    10
    """
    basic_attack = 'tackle'
    damage = 40

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, 'used', self.basic_attack, 'on', other.name + '!')
            other.hp = max(0, other.hp - self.damage)
            if other.hp == 0:
                print(other.name, 'fainted!')

squirt = Pokemon('Squirtle', 'Marvin')
bulba = Pokemon('Bulbasaur', 'Brian')


from random import random

class ElectricType(Pokemon):
    """An electric-type Pokemon class.

    >>> import random; random.seed(0)  # For determinism
    >>> pika = ElectricType('Pikachu', 'Marvin')  # Pokemon.__init__
    >>> pika.basic_attack  # Found in ElectricType
    'thunder shock'
    >>> pika.speak()  # Found in Pokemon
    Pikachu!
    >>> squirt.attack(bulba)
    Squirtle!
    Squirtle used tackle on Bulbasaur!
    >>> pika.attack(squirt)  # Found in ElectricType
    Pikachu!
    Pikachu used thunder shock on Squirtle!
    >>> squirt.hp
    10
    >>> pika.attack(bulba)
    Pikachu!
    Pikachu used thunder shock on Bulbasaur!
    Bulbasaur fainted!
    """
    basic_attack = 'thunder shock'
    prob = 0.1

    def attack(self, other):
        Pokemon.attack(self, other)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')

pika = ElectricType('Pikachu', 'Marvin')


# Zapdos multiple inheritance example

class FlyingType(Pokemon):
    """A flying-type Pokemon class.

    >>> pidg = FlyingType('Pidgey', 'Brian')
    >>> pidg.basic_attack
    'peck'
    >>> pidg.fly('Pallet Town')
    Brian flew to Pallet Town
    """
    basic_attack = 'peck'
    damage = 35
    def fly(self, location):
        print(self.trainer, 'flew to', location)

pidg = FlyingType('Pidgey', 'Brian')


class Zapdos(ElectricType, FlyingType):
    """A class representing the Pokemon Zapdos.

    >>> zap = Zapdos('big bird', 'Marvin')  # Pokemon.__init__
    >>> zap.speak()  # Found in Zapdos
    EEEEEEEE
    >>> zap.fly('Lavender Town')  # Found in FlyingType
    Marvin flew to Lavender Town
    >>> zap.attack(pidg)  # Found in ElectricType
    EEEEEEEE
    big bird used thunder on Pidgey!
    Pidgey fainted!
    """
    basic_attack = 'thunder'
    damage = 120
    def speak(self):
        print('EEEEEEEE')

zap = Zapdos('big bird', 'Marvin')


# Exceptions (the following are all commented out because they error)

# 1 / 0
# square
# assert 0 == 1, 'why not'
# raise TypeError("I'm typing all wrong")
# raise 1  # errors, but not how you intended

class MySpecialException(Exception):
    def __init__(self, msg):
        self.msg = msg

# raise MySpecialException('not that special')

def safe_invert(x):
    """Return the inverse of x, unless x is 0.

    >>> safe_invert(2)
    0.5
    >>> safe_invert(0)
    Nope
    """
    try:
        return 1 / x
    except ZeroDivisionError:
        print('Nope')


# Implementing arithmetic operators for rational numbers

from fractions import gcd

class Rational:
    """A rational number class that implements magic methods
    for arithmetic operators.

    >>> x, y = Rational(3, 5), Rational(1, 3)
    >>> x.value
    0.6
    >>> x + y
    Rational(14, 15)
    >>> print(x + y)
    14 / 15
    >>> print(x * y)
    1 / 5
    >>> print(x - y)
    4 / 15
    """
    def __init__(self, numer, denom):
        divisor = gcd(numer, denom)  # Reduce to lowest terms
        self.n = numer // divisor
        self.d = denom // divisor

    @property
    def value(self):
        return self.n / self.d

    def __repr__(self):
        return 'Rational(' + str(self.n) + ', ' + str(self.d) + ')'

    def __str__(self):
        return str(self.n) + ' / ' + str(self.d)

    def __add__(self, other):
        numer = self.n * other.d + other.n * self.d
        denom = self.d * other.d
        return Rational(numer, denom)

    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)

    def __sub__(self, other):
        numer = self.n * other.d - other.n * self.d
        denom = self.d * other.d
        return Rational(numer, denom)


# Custom containers

class Dict:
    """A custom dictionary class that implements the
    mutable container protocol.

    >>> d = Dict([1, 'a', True, 4], [5, 2, [1, 2, 3], 'hello'])
    >>> len(d)
    4
    >>> d[1]
    5
    >>> 4 in d
    True
    >>> d['a'] = 'hi'
    >>> d['a']
    'hi'
    >>> del d['a']
    >>> len(d)
    3
    """
    def __init__(self, keys=[], values=[]):
        assert len(keys) == len(values), 'Lengths must match!'
        self.keys = keys
        self.values = values

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, key):
        try:
            i = self.keys.index(key)
            return self.values[i]
        except ValueError:
            raise KeyError(str(key) + 'does not exist!')

    def __contains__(self, key):
        return key in self.keys

    def __setitem__(self, key, value):
        try:
            i = self.keys.index(key)
            self.values[i] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def __delitem__(self, key):
        try:
            i = self.keys.index(key)
            self.keys.pop(i)
            self.values.pop(i)
        except ValueError:
            raise KeyError(str(key) + 'does not exist!')
