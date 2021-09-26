from multiprocessing import Pool

def f(x: int) -> int:
    return x * x

if __name__ == '__main__':
    with Pool() as pool:
        pool.map(f, range(1_000_000_000))

        print('Done')
