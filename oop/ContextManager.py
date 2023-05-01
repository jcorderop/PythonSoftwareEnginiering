class MyHandler:
    def __init__(self, name):
        self.name = name
        print('Initiation class: {}'.format(name))

    def __enter__(self):
        print('Context Handler Validations: {}'.format(self.name))
        # validations
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context Handler Finished: {}'.format(self.name))
        print('exc_type: {}'.format(exc_type))
        print('exc_val : {}'.format(exc_val))
        print('exc_tb  : {}'.format(exc_tb))

    def do_something(self):
        print(f'Doing something with... {self.name}')


with MyHandler('Jorge') as m: #__init__
    m.do_something()  #__enter__
    #__exit__