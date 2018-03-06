# Primitive expressions

2016
201.6
'Hello world!'
True
False
[2, 0, 'one', 'six']


# Operators

2000 + 16
2000 + 4 ** 2
4032 // 2
1 * 2 * 3 * 4 + 5 ** 6 // 7 - 8 * 9 - 10 - 11 * 12 - 13 - 14 - 15 + 16
'Hello ' + 'world!'
[2, 0] + ['one', 'six']


# Call expressions

from operator import add, mul
add(2000, 16)
mul(1008, 2)
abs(-2016)
pow(2, 100)

from math import sqrt
sqrt(2016)

from math import sin, pi
sin(pi)


# Nested call expressions

add(add(2, mul(4, 6)), mul(3, 5))


# Shakespeare demo
# Note: Download from http://composingprograms.com/shakespeare.txt

shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:15]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

words = set(text)  # Sets have no repeated elements
len(words)
max(words)
max(words, key=len)

'draw'[::-1]  # Reversing a word
{w for w in words if w == w[::-1] and len(w) > 4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
