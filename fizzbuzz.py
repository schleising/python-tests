for i in range(100):
    x = i + 1
    s = ''
    fizz = 3
    buzz = 5

    if x % fizz == 0:
        s = s + 'fizz'

    if x % buzz == 0:
        s = s + 'buzz'

    if s == '':
        s = str(x)

    print(f'{x:3}: {s}')
