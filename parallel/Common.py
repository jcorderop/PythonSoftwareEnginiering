
import math
from threading import current_thread

NUMBERS = [
    100_000_000_019,
    100_000_000_019,
    100_000_000_019,
    100_000_000_019
]


def is_prime(number):
    print('Thread Name: {}, number: {}'.format(current_thread(), number))
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    for i in range(2, int(sqrt_number) + 1):
        if (number_float / i).is_integer():
            result = False
            break
    result = True
    print('Thread Name: {}, result: {}'.format(current_thread(), result))
    return result