import asyncio
import time


async def asleep(shall_fail=False):
    if not shall_fail:
        await asyncio.sleep(2)
        print("ping")
    else:
        try:
            raise ValueError
        finally:
            print("pong")


async def main():
    # start = time.monotonic()

    # await asleep()
    # await asleep()

    # print(time.monotonic() - start)  # 4.00242374278605

    # start = time.monotonic()

    # task1 = asyncio.create_task(asleep())
    # task2 = asyncio.create_task(asleep())

    # await task1
    # await task2

    # print(time.monotonic() - start)  # 2.0017966832965612

    start = time.monotonic()

    task1 = asyncio.create_task(asleep())
    task2 = asyncio.create_task(asleep())

    await task1
    task1.cancel()
    await task2


asyncio.run(main())
