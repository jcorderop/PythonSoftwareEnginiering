from parallel.Common import is_prime, NUMBERS
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def worker(sleep_time: float) -> None:
    print("Starting a worker...")
    time.sleep(sleep_time)
    print("End working...")


t1 = Thread(target=worker,
            name='T1',
            args=(2.0,))

print('New Thread...')
print(f'ident: {t1.ident}')
print(f'alive: {t1.is_alive()}')
print(f'name : {t1.name}')

t1.start()

print('Started Thread...')
print(f'ident: {t1.ident}')
print(f'alive: {t1.is_alive()}')
print(f'name : {t1.name}')

t1.join()


print('\n\n Multiple threads')
def sequential():
    print('\n\nPerforming with No threads...')
    l1 = time.perf_counter_ns()
    for number in NUMBERS:
        is_prime(number)
    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')


def multi_threading():
    print('\n\nPerforming with Multi threads...')
    l1 = time.perf_counter_ns()
    threads = [Thread(target=is_prime,
                      name='T{}'.format(number),
                      args=(NUMBERS[number],)) for number in range(len(NUMBERS))]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')


print('\n\n ThreadPool')
def thread_pool():
    print('\n\nPerforming with Multi threads...')
    l1 = time.perf_counter_ns()
    with ThreadPoolExecutor(max_workers=4) as ex:
        for number, prime in zip(NUMBERS, ex.map(is_prime, NUMBERS)):
            print(f'{number} is prime {prime}')

    latency = (time.perf_counter_ns() - l1) / 1e06
    print(f'Latency: {latency}')


if __name__ == '__main__':
    sequential()
    multi_threading()
    thread_pool()
    print('Finished...')
