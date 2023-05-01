import time
from multiprocessing import Process, Pool

from parallel.Common import is_prime, NUMBERS


def multi_processing():
    print('\n\nPerforming with Multi Processes...')
    l1 = time.perf_counter_ns()
    processes = [Process(target=is_prime,
                         args=(NUMBERS[number],)) for number in range(len(NUMBERS))]
    [p.start() for p in processes]
    [p.join() for p in processes]
    [p.close() for p in processes]

    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')


def multi_processing_pool():
    print('\n\nPerforming with Multi Processes Pool...')
    l1 = time.perf_counter_ns()
    with Pool() as pool:
        result = pool.map(is_prime, NUMBERS)
    print(result)

    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')


if __name__ == '__main__':
    multi_processing()
    multi_processing_pool()
    print('Finished...')