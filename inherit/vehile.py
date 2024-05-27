# 2. Sukurkite bazinę klasę Vehicle su atributais make ir model ir metodu description(),
# kuris juos atspausdina. Sukurkite išvestinę klasę Car, kuri priima atributą year ir
# naudoja super(), kad iškviestų bazinės klasės metodą savo aprašymo metode.

class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def description(self):
        print(f"Vehicle {self.make}, {self.model}.")


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int):
        self.year = year
        super().__init__(make, model)

    def describe(self):
        super().description()
        print(f"The car: {self.make}, {self.model}, {self.year}")


car_1 = Car('Audi', 'X', 2016)
car_1.description()
car_1.describe()