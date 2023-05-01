from dataclasses import dataclass, field


@dataclass(slots=True)
class User:
    name: str
    age: int
    address: str

print('Simple dataclass...')
user = User('jorge', 20, 'Switzerland')
print(user)


@dataclass(slots=True)
class UserOrders:
    name: str
    age: int
    address: str
    active: bool = True
    orders: list[str] = field(default_factory=list,
                              compare=False,
                              hash=False,
                              repr=False)
print('\n\nComplex dataclass...')
user_orders = UserOrders('jorge', 20, 'Switzerland')
print(user_orders)
print(id(user_orders.orders))

print('\n\nComplex dataclass...')
user_orders2 = UserOrders('jorge', 20, 'Switzerland')
print(user_orders2)
print(id(user_orders2.orders))