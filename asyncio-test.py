import asyncio
import time

def count(input: int):
    print(f"One: {input}")
    time.sleep(1)
    print(f"Two: {input}")

async def main():
    loop = asyncio.get_event_loop()
    print(f'Main Loop: {loop}')
    futures = [loop.run_in_executor(None, count, i) for i in range(48)]
    for future in futures: print(future)
    time.sleep(1)
    for future in futures: await future
    # print(results)

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f'Outer Loop: {loop}')
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
