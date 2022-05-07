def t1(zs):
    xs, ys = zip(*zs)
    return list(xs), list(ys)

def t2(zs):
    xs, ys = [], []
    for x, y in zs:
        xs.append(x)
        ys.append(y)
    return xs, ys

def t3(zs):
    xs = [x for x, y in zs]
    ys = [y for x, y in zs]
    return xs, ys

if __name__ == '__main__':
    from timeit import timeit
    setup_string='''\
N = 200000
xs = list(range(1, N))
ys = list(range(N+1, N*2))
zs = list(zip(xs, ys))
from __main__ import t1, t2, t3
'''
    print(f'zip:\t\t{timeit("t1(zs)", setup=setup_string, number=1000)}')
    # print(f'append:\t\t{timeit("t2(zs)", setup=setup_string, number=1000)}')
    print(f'list comp:\t{timeit("t3(zs)", setup=setup_string, number=1000)}')
