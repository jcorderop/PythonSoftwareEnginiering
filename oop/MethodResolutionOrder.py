class A:
    def __init__(self):
        print('init A')

class B(A):
    def __init__(self):
        super().__init__()
        print('init B')

class C(A):
    def __init__(self):
        super().__init__()
        print('init C')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('init D')

print('--------------')
a = A()
print('--------------')
b = B()
print('--------------')
c = C()
print('--------------')
d = D()


print('--------------')
print('--------------')
print(D.mro())