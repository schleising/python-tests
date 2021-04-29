import asyncio
import time

def sleeper(funcNum: int) -> list[int]:
    print(f'Enterred {funcNum}')
    time.sleep(1)
    print(f'Exiting {funcNum}')
    return [funcNum, funcNum * 10]

async def main() -> None:
    print(1)
    futures = [asyncio.to_thread(sleeper, count) for count in range(1,60)]
    print(2)
    results = await asyncio.gather(*futures)
    print(3)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())
    print('Done')
