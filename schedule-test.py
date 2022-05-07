import time
from schedule import Scheduler

scheduler = Scheduler()

def main() -> None:
    scheduler.every(2).seconds.do(hello, 'Steve')

    while True:
        scheduler.run_pending()
        time.sleep(0.01)

def hello(name: str) -> None:
    print(f'Hello {name}: {time.time()}')

if __name__ == '__main__':
    main()
