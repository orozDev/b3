class A:
    def __new__(cls, *args, **kwargs):
        print('1')
        cls.__init__(cls, *args, **kwargs)
        return cls

    def __init__(self, arg):
        self.arg = arg
        print('2')



o = A('arg')