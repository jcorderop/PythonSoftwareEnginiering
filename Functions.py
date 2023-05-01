from typing import Any, Optional


# args
print('\n# args')
def my_func_args(a: Any, *args: Any) -> None:
    print(*args, type(args))
    print(f'a: {a}, args: {args}')

my_func_args('a', 'b', 'c', 'd', 'e')


# kwargs
print('\n# kwargs')
def my_func_kwargs(a: Any, **kwargs: Any) -> None:
    print(*kwargs, type(kwargs))
    print(f'a: {a}, args: {kwargs}')

my_func_kwargs('a', b='b1', c='c1', d='d1', e='e1')


# optional
print('\n# optional')
def func_add(value: Any, my_list: Optional[list] = None):
    if my_list:
        my_list.append(value)
    else:
        my_list = [value]
    return my_list

print(func_add(20))
print(func_add(20, []))


print('\n# Standard arguments')
print('/ -> it is used to disable pass arguments using the name of the argument')
def my_func_disable_use_name_param(value: Any, /):
    print(value)
my_func_disable_use_name_param('a')
print('OK')
try:
    my_func_disable_use_name_param(value='a')
except Exception as e:
    print('ERROR: ', e)


print('* -> it is used to force to use name of the argument')
def my_func_force_use_name_param(*, value: Any):
    print(value)
try:
    my_func_force_use_name_param('a')
except Exception as e:
    print('ERROR: ', e)
my_func_force_use_name_param(value='a')
print('OK')


