def say_hello():
    print('Hello world!')


say_hello()

var = say_hello

var()


def sum(a, b, c=1, *args, **kwargs):
    print(len(kwargs))
    print(args)
    return a + b + c

nums = [12, 12, 43,324, 324, 234, 23, 42, 3423423, 32423, 4234]

res = sum(*nums, e=1, d=1)

print(res)