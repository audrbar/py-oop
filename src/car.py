class Car:
    def __init__(self, maker, model, color):
        self.maker = maker
        self.model = model
        self.color = color

    def drive(self):
        print(f'The car {self.maker} is driving.')

    def start_engine(self):
        print(f'The car {self.color} {self.maker} {self.model} now works.')


car_1 = Car('audi', 'A4', 'green')
car_2 = Car('bmw', 'x1', 'red')
car_1.drive()
car_2.drive()
car_1.start_engine()
car_2.start_engine()
