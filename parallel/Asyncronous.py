import asyncio
import time


async def heavy_call() -> int:
    print('starting heavy_call...')
    await asyncio.sleep(2.0)
    print('end heavy_call...')
    return 0


async def super_heavy_call() -> int:
    print('starting super_heavy_call...')
    await asyncio.sleep(4.0)
    print('end super_heavy_call...')
    return 0


async def main_wait() -> int:
    print('starting super_heavy_call...')
    await heavy_call()
    print('end super_heavy_call...')
    return 0


async def calling_tasks() -> int:
    l1 = time.perf_counter_ns()
    task1 = asyncio.create_task(heavy_call())
    task2 = asyncio.create_task(super_heavy_call())
    res_task2 = await task2
    res_task1 = await task1
    print(f'task1: {res_task1}')
    print(f'task2: {res_task2}')
    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')
    return 0


async def calling_gather() -> int:
    l1 = time.perf_counter_ns()
    res_tasks = await asyncio.gather(heavy_call(), super_heavy_call())
    print(f'res_tasks: {res_tasks}')
    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')
    return 0


if __name__ == '__main__':
    print(f'\n\ncalling async')
    code = asyncio.run(main_wait())

    print(f'\n\ncalling tasks')
    code_task = asyncio.run(calling_tasks())

    print(f'\n\ncalling gather')
    code_gather = asyncio.run(calling_tasks())

