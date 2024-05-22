class Car:
    def __init__(self, maker, model, color):
        self.maker = maker
        self.model = model
        self.color = color
    def drive(self):
        print('The car is driving.')
    def start_engine(self):
        print(f'The car {self.maker} {self.model} now works.')

car_1 = Car('audi','A4','green')
car_2 = Car('bmw','x1','red')
print(f'The first car: {car_1.model},{car_1.maker},{car_1.color}')
print(f'The second car: {car_2.model},{car_2.maker},{car_2.color}')
print(car_1.start_engine())
print(car_2.start_engine())