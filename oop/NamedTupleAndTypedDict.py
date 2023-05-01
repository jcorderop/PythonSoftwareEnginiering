
from typing import NamedTuple
from typing import TypedDict


class User(NamedTuple):
    name: str
    age: int
    is_admin: bool = False


print('NamedTuple...')
user = User(name='Jorge', age=20, is_admin=True)
print(user)


class User2(TypedDict):
    name: str
    age: int
    is_admin: bool


print('Created from a dict...')
user2: User2 = {'name': 'Jorge',
                'age': 20,
                'is_admin': True}
print(user2)
print(type(user2))
user2['last'] = 'Cordero'
print(user2)