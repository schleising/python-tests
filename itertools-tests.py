from itertools import product, zip_longest
from pathlib import Path

l1 = [
    'C',
    'H',
    'M',
    'L',
]

l2 = [
    '1',
    '2',
    '3',
    '4',
    '5',
]

print([''.join(pair) for pair in product(l1, l2)])

print([item for item in zip_longest(l1, l2, fillvalue='')])

print('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ')
print(len('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'))
print('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'.lower())
print('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'.casefold())

print(Path.home())
