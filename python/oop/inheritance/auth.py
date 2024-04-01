from uuid import uuid4


class BaseUser:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class User(BaseUser, Person):
    ADMIN = 'admin'
    CLIENT = 'client'

    ROELS = (
        (CLIENT, 'Клиент'),
        (ADMIN, 'Адимин')
    )

    def __init__(self, username, password, email, first_name, last_name, age, role):
        super().__init__(username, password, email)
        Person.__init__(self, first_name, last_name, age)

        if role not in [self.ADMIN, self.CLIENT]:
            raise ValueError(f'Роль "{role}" не существует')
        self.role = role

    def get_role(self):
        for key, name in self.ROELS:
            if key == self.role:
                return name
        return None

    from uuid import uuid4

    class BaseUser:

        def __init__(self, username, password, email):
            self.username = username
            self.password = password
            self.email = email

    class Person:

        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

        def get_full_name(self):
            return f'{self.first_name} {self.last_name}'

    class User(BaseUser, Person):
        ADMIN = 'admin'
        CLIENT = 'client'

        ROELS = (
            (CLIENT, 'Клиент'),
            (ADMIN, 'Адимин')
        )

        def __init__(self, username, password, email, first_name, last_name, age, role):
            super().__init__(username, password, email)
            Person.__init__(self, first_name, last_name, age)

            if role not in [self.ADMIN, self.CLIENT]:
                raise ValueError(f'Роль "{role}" не существует')
            self.role = role

        def get_role(self):
            for key, name in self.ROELS:
                if key == self.role:
                    return name
            return None

        def get_full_name(self):
            name = Person.get_full_name(self)
            return f'{name} - {self.get_role()}'

    class AnonymousUser:

        def __init__(self):
            pass

    users = [User(
        'oroz',
        'qwerty',
        'oroz@gmail.com',
        'Orozbek',
        'Zhenishbekov',
        12,
        User.CLIENT
    )]

    class AuthSystem:

        def __init__(self):
            self.is_authenticated = False
            self.user = AnonymousUser()
            self.key = None

        def __get_key(self) -> str:
            return str(uuid4())

        def login(self, username: str, password: str) -> dict:
            assert type(username) is str
            assert type(password) is str

            temp = list(filter(lambda user_: username == user_.username, users))
            if len(temp) > 0:
                user = temp[0]
                if user.password == password:
                    self.user = user
                    self.key = self.__get_key()
                    self.is_authenticated = True
                    return {
                        'is_authenticated': True,
                        'user': user,
                        'key': self.key
                    }
            return {
                'is_authenticated': False,
                'user': None,
                'key': None
            }

        def authenticate(self, key: str):
            assert type(key) is str
            return self.key == key

    auth = AuthSystem()
    auth.login('oroz', 'qwerty')

    print(auth.key)

    print(auth.authenticate(input('Enter key: ')))

    def get_full_name(self):
        name = Person.get_full_name(self)
        return f'{name} - {self.get_role()}'


class AnonymousUser:

    def __init__(self):
        pass


users = [User(
    'oroz',
    'qwerty',
    'oroz@gmail.com',
    'Orozbek',
    'Zhenishbekov',
    12,
    User.CLIENT
)]


class AuthSystem:

    def __init__(self):
        self.is_authenticated = False
        self.user = AnonymousUser()
        self.key = None

    def __get_key(self) -> str:
        return str(uuid4())

    def login(self, username: str, password: str) -> dict:
        assert type(username) is str
        assert type(password) is str

        temp = list(filter(lambda user_: username == user_.username, users))
        if len(temp) > 0:
            user = temp[0]
            if user.password == password:
                self.user = user
                self.key = self.__get_key()
                self.is_authenticated = True
                return {
                    'is_authenticated': True,
                    'user': user,
                    'key': self.key
                }
        return {
            'is_authenticated': False,
            'user': None,
            'key': None
        }

    def authenticate(self, key: str):
        assert type(key) is str
        return self.key == key


auth = AuthSystem()
auth.login('oroz', 'qwerty')


print(auth.key)

print(auth.authenticate(input('Enter key: ')))

