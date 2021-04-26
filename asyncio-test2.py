import asyncio
import time

def sleeper(funcNum: int) -> None:
    print(f'Enterred {funcNum}')
    time.sleep(1)
    print(f'Exiting {funcNum}')

async def main() -> None:
    print(1)
    futures = [asyncio.to_thread(sleeper, count) for count in range(6)]
    print(2)
    await asyncio.gather(*futures)
    print(3)

if __name__ == '__main__':
    asyncio.run(main())