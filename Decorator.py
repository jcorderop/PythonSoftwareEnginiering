from functools import wraps
from typing import Any, Callable


print('Simple decorator')
def outer_fn(fn: Callable) -> Callable:
    def inner_fn() -> Any:
        fn_result = fn()
        return fn_result
    return inner_fn

def any_fn_simple():
    print('hallo...')

def any_fn(name):
    print(f'hallo... {name}')

print('-------Simple callback-------')
my_dec = outer_fn(any_fn_simple)
my_dec()

print('\n\nDecorator template')
def my_decorator(fn: Callable) -> Callable:
    print('Start decorator from fn: {}'.format(fn.__name__))
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('Start wrapper from fn: {}'.format(fn.__name__))
        fn_result = fn(*args, **kwargs)
        print('End wrapper from fn: {}'.format(fn.__name__))
        return fn_result
    print('End decorator from fn: {}'.format(fn.__name__))
    return wrapper

@my_decorator
def any_fn_deco(name):
    print(f'>>>> hallo decorator... {name}')

print('-------Decorator callback-------')
fn_callback = my_decorator(any_fn)
fn_callback('pepe')

print('-------Decorator @ name-------')
any_fn_deco('pepe')



print('\n\nDecorator debugger')
def debugger(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('debugger args: {}'.format(args))
        print('debugger kwargs: {}'.format(kwargs))
        fn_result = fn(*args, **kwargs)
        return fn_result
    return wrapper

@debugger
def any_fn_deco_debug(name, last_name, cp):
    print(f'>>>> hallo debug decorator... {name} {last_name}, cp {cp}')

any_fn_deco_debug('jorge', last_name='cordero', cp=8501)

