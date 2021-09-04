from weakref import finalize

class Person:
    pass

def test():
    kenny = Person()
    finalize(kenny, print, 'You killed Kenny !!')

test()

bobby = Person()
finalize(bobby, print, 'Bobby Dead')

print('Entering loop')

while True:
    pass
