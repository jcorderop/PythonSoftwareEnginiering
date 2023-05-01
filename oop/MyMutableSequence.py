from collections.abc import MutableSequence
from typing import Any


class MyMutableSequence(MutableSequence):

    def __init__(self, values=None):
        super().__init__()
        if values:
            self._values = values
        else:
            self._values = []

    def __getitem__(self, index: int) -> Any:
        print('__getitem__...')
        return self._values[index]

    def __setitem__(self, index: int, value: Any) -> None:
        print('__setitem__...')
        self._values[index] = value

    def __delitem__(self, index: int) -> None:
        print('__delitem__...')
        del self._values[index]

    def __len__(self) -> int:
        print('__len__...')
        return len(self._values)

    def insert(self, index: int, value: Any) -> None:
        print('inserting...')
        self._values.insert(index, value)

    def __repr__(self):
        return str(self._values)

print('MutableSequence...')
my_seq = MyMutableSequence()

print('--- insert ---')
my_seq.append(1)
my_seq.append(2)
my_seq.append(3)
my_seq.append(4)
print(len(my_seq))
print(my_seq)

print('--- del ---')
del my_seq[2]
print(len(my_seq))
print(my_seq)

print('--- get ---')
print(my_seq[2])

print('--- set ---')
my_seq[2] = 3
print(len(my_seq))
print(my_seq)


