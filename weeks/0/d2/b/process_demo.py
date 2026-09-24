"""
Искал решение без помощи ИИ, только справочные данные из поиска.

"""
import concurrent.futures
import os
import time

print(f"Parent PID: {os.getpid()}")


def func():
    start = time.monotonic()
    print(f"Child PID: {os.getpid()}, Child PPID: {os.getppid()}")

    while time.monotonic() - start < 5:
        pass


executor = concurrent.futures.ProcessPoolExecutor(max_workers=1)
executor.submit(func)

while True:
    pass
