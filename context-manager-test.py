from time import sleep
import timeit
import atexit

class Timer():
    def __init__(self) -> None:
        self.startTime: float = 0.0

    def __enter__(self):
        self.startTime = timeit.default_timer()

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type == ValueError:
            print(exc_value)
        print(f'Elapsed Time: {timeit.default_timer() - self.startTime}')

@atexit.register
def PrintExit():
    print('Exiting Programme...')

with Timer():
    sleep(10)

with Timer():
    sleep(0.5)
