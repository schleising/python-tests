class A(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return f'Object {self.name} of Class A'

class B(A):
    def __str__(self):
        return f'Object {self.name} of Class B'

class C(A):
    def __str__(self):
        return f'Object {self.name} of Class C'

def func1(a: A):
    print(f'First Test: {a}')

    match a:
        case B():
            b = a
            print(f'a: {a}')
            print(f'b: {b}')
        case C():
            c: C = a
            print(f'a: {a}')
            print(f'c: {c}')
        case A():
            print(f'a: {a}')
        case _:
            print('Unsupported Type')

    print(f'Last Test: {a}')

def func2(a: A):
    print(f'First Test: {a}')

    if isinstance(a, B):
        b = a
        print(f'a: {a}')
        print(f'b: {b}')
    elif isinstance(a, C):
        c = a
        print(f'a: {a}')
        print(f'b: {c}')
    elif isinstance(a, A):
        print(f'a: {a}')
    else:
        print('Unsupported Type')

    print(f'Last Test: {a}')

a = A('1')
b = B('2')
c = C('3')

print('Checking using structural pattern matching')
func1(a)
func1(b)
func1(c)
# func(1)

print()
print('Checking using isinstance()')
func2(a)
func2(b)
func2(c)
