class PowerOfIterator:
    def __init__(self, N: int, pow: int):
        self.N = N
        self.pow = pow

    def __iter__(self):
        self.current_n = 0
        return self

    def __next__(self):
        if self.current_n <= self.N:
            current_result = self.pow**self.current_n
            self.current_n += 1
            return current_result
        else:
            raise StopIteration

print('Iterators...')
p = PowerOfIterator(10, 2)

for i in p:
    print(i)

p_list = [x for x in PowerOfIterator(10, 2)]
print(p_list)

# Generator
def PowerOfGenerator(N: int, pow: int):
    current_n = 0
    while current_n <= N:
        yield 2**current_n
        current_n += 1

print('Generator...')
p = PowerOfGenerator(10, 2)

for i in p:
    print(i)

p_list = [x for x in PowerOfGenerator(10, 2)]
print(p_list)