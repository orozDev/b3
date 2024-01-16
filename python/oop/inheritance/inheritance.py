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
        super(BaseUser, self).__init__(username, password, email)
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


oroz = User(
    'oroz',
    'qwerty',
    'oroz@gmail.com',
    'Orozbek',
    'Zhenishbekov',
    12,
    User.CLIENT
)

print(oroz.get_full_name())