from enum import Enum, IntEnum


class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Colors.BLUE)
print(issubclass(Colors, int))


class Colors2(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(issubclass(Colors2, int))

print(list(Colors2))