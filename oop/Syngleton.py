
class Something:

    def __new__(cls, name, *args, **kwargs):
        print('Creating Instance: {}'.format(name))
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print('Initiating Instance: {}'.format(name))

print('------------Using New------------')
Something('Jorge')

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        else:
            print('Already Initiated...')
        return cls._instance


print(id(Singleton()))
print(id(Singleton()))