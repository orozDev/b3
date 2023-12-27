class Car:
    # brand - Свойства

    def __init__(self, brand, model, color, price, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.year = year
        self.is_started = False

    def start(self):
        self.is_started = True
        print(f'{self.brand} {self.model} has been started')

    def stop(self):
        if self.is_started:
            print(f'{self.brand} {self.model} has been stopped')
        else:
            print(f'Before that you should start the car {self.brand} - {self.model}')

    def restart(self):
        self.stop()
        self.start()

    # def method(self): - Методы
    #     pass


bmw = Car(
    'BMW', 'M5', 'black', 10000, 2010
)

camry = Car(
    'Toyota', 'Camry 3.5', 'white', 12000, 2016
)

camry.start()
camry.stop()

# camry.restart()

# print(
#     f'{camry.brand} - {camry.model}'
# )
