
USER = 'admin'
PASSWORD = 'qwerty'

username = input('Enter username: ')
password = input('Enter password: ')

is_authenticated = USER == username and password == PASSWORD


def _is_authenticated(func):
    def inner_func(*args, **kwargs):
        if is_authenticated:
            func(*args, **kwargs)
        else:
            print('The user must be authenticated')

    return inner_func


@_is_authenticated
def say_hello(name=USER):
    print(f'{name}, Hello World!')


@_is_authenticated
def say_goodbye():
    print('Good bye World!')


say_hello('oroz')