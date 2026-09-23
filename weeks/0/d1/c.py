# Всё же предлагаю отдельно преподать решение такой задачи, я искренне не понимаю как это решить за оставшееся время
import asyncio
import typing


async def simple_job():
    return "completed"


async def sleep_job(tts):
    await asyncio.sleep(tts)
    return "completed"


async def exception_job():
    raise ValueError


async def run_jobs(jobs: list[typing.Callable], max_concurrency: int) -> list[str]:
    ...


async def main():
    print("long " + await sleep_job(5))
    print(await simple_job())


asyncio.run(main())
