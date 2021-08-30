for i in range(100):
    x = i + 1
    s = ''

    entries = {
        'fizz': 3,
        'buzz': 5,
    }

    for entry, value in entries.items():
        if x % value == 0:
            s += entry

    if s == '':
        s = str(x)

    print(f'{x:3}: {s}')
