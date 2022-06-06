from concurrent.futures import ProcessPoolExecutor, Future, ThreadPoolExecutor
import math
# import os
import threading
from time import sleep
from typing import Any

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095291,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n: int) -> tuple[int, bool]:
    print(f'{threading.get_ident()} Calculating {n}')
    if n == 112272535095293:
        sleep(5)
    # else:
    #     sleep(1)

    if n < 2:
        return n, False
    if n == 2:
        return n,True
    if n % 2 == 0:
        return n, False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return n, False
    return n, True

def printResult(fut: Future[tuple[int, bool]]):
    num, is_prime = fut.result()
    print(f'{threading.get_ident()} {num} is Prime: {is_prime}')

def main():
    results = []
    with ThreadPoolExecutor() as executor:
        for num in PRIMES:
            result = executor.submit(is_prime, num)
            sleep(1)
            result.add_done_callback(printResult)
            results.append(result)

        for i in range(25):
            print(f'{threading.get_ident()} {i:02}')
            sleep(0.25)

    print(f'{threading.get_ident()} Pool closed')
    # print(f'{1.5 / 1}')

if __name__ == '__main__':
    main()
