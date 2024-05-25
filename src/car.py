class Car:
    wheels: int = 4
    total_cars: int = 0

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        print(f"The {self.color} car '{self.brand}' '{self.model}' was created.")
        Car.total_cars += 1

    def start_engine(self) -> str:
        return f"The {self.color} car '{self.brand}' '{self.model}' engine ir now running."


car_1 = Car('audi', 'A4', 'green')
car_2 = Car('bmw', 'x1', 'red')
car_3 = Car('Kia', 'Y', 'white')
print(f"Cars created since: {Car.total_cars}")
print(f"All of them have {car_1.wheels} wheels.")
print(car_1.start_engine())
print(car_2.start_engine())
print(car_3.start_engine())
