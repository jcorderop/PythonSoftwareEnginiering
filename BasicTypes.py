import math


def print_float(value):
    print(f'{value:.32f}')


my_fraction_2 = 1 / 10 + 1 / 10 + 1 / 10
print_float(my_fraction_2)

my_fraction_3 = 0.3
print_float(my_fraction_3)


def float_is_equal(x, y):
    epsilon = 1e-15
    difference = math.fabs(x - y)
    return difference < epsilon


result1 = my_fraction_2 == my_fraction_3
print('result: {}'.format(result1))

result2 = float_is_equal(my_fraction_2, my_fraction_3)
print('result: {}'.format(result2))

result3 = math.isclose(my_fraction_2, my_fraction_3)
print('result: {}'.format(result3))


my_bool = True
my_int = 1

print('value equality (==) {}'.format(my_bool == my_int))
print('value equality (==) {}'.format(my_bool == True))
print('value equality (==) {}'.format(1 == my_int))
print('address memory equality {}'.format(my_bool is my_int))
print('address memory equality {}'.format(my_bool is True))
print('address memory equality {}'.format(1 is my_int))