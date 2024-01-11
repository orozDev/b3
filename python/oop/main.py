class Car:

    # def __new__(cls, *args, **kwargs):
    #     print(args, kwargs)
    #

    def __init__(self, brand, model, color, year, price):
        print(2)
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.is_started = False

    def get_full_name(self):
        return f'{self.brand} {self.model}'

    def start(self):
        if not self.is_started:
            print(f'The car {self.get_full_name()} has been started!')
            self.is_started = True
        else:
            print('The car is already started')

    def stop(self):
        if self.is_started:
            print(f'The car {self.get_full_name()} has been stopped!')
            self.is_started = False
        else:
            print('Before that the car must be started')

    def __str__(self):
        return self.get_full_name()


bmw = Car(
    'BMW',
    'M5F90',
    'Black',
    2022,
    80000,
)

# bmw.start()
# bmw.start()
# bmw.stop()
# bmw.start()
# bmw.stop()
# bmw.stop()


print(
    bmw.__dict__,
    bmw.__str__(),
    sep='\n'
)

print(bmw)