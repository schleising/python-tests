from multiprocessing import Pool

def f(x: int) -> int:
    a = x

    for i in range(100_000_001):
        a += i * i
        if i % 10_000_000 == 0:
            print(f'{x}: {a}')

    return a

if __name__ == '__main__':
    with Pool() as pool:
        pool.map(f, range(8))

        print('Done')
