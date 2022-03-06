from weakref import finalize

class Person:
    pass

def test():
    kenny = Person()
    finalize(kenny, print, 'You killed Kenny !!') # type: ignore

test()

bobby = Person()
finalize(bobby, print, 'Bobby Dead') # type: ignore

print('Entering loop')

while True:
    pass
