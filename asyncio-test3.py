import asyncio
import time

async def say_after(delay, what):
    print(f'In task {delay}')
    time.sleep(delay)
    print(f'{what}: {time.strftime("%X")}')

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))
    print(f"started at {time.strftime('%X')}")
    time.sleep(4)
    print(f"continued at {time.strftime('%X')}")

    await task1

    print(f"middle {time.strftime('%X')}")

    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
