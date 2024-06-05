from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return round((3.14 * (self.radius ** 2)), 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, ilgis: int, plotis: int):
        self.ilgis = ilgis
        self.plotis = plotis

    def area(self):
        return self.ilgis * self.plotis

    def perimeter(self):
        return (self.ilgis + self.plotis) * 2


class Triangle(Shape):
    def __init__(self, kr_ilgis: int, aukstine: int):
        self.kr_ilgis = kr_ilgis
        self.aukstime = aukstine

    def area(self):
        return self.kr_ilgis * self.aukstime / 2

    def perimeter(self):
        return self.kr_ilgis * 2 + self.aukstime


rect = Rectangle(2, 5)
circ = Circle(5)
tria = Triangle(5, 4)
print(f"Staciakampio plotas: {rect.area()}, perimetras: {rect.perimeter()}")
print(f"Apskritimo plotas: {circ.area()}, perimetras: {circ.perimeter():.2f}")
print(f"Trikampio plotas: {tria.area()}, perimetras: {tria.perimeter()}")
