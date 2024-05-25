class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def describe(self):
        print(f'Your animal is {self.name}, {self.species}.')


animal_1 = Animal('cat', 'mammal')
animal_1.describe()
