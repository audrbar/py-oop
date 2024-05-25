class Rectangle:
    def __init__(self, ilgis: int, plotis: int):
        self.ilgis = ilgis
        self.plotis = plotis

    def get_area(self) -> int:
        return self.ilgis * self.plotis

    def get_perimeter(self) -> int:
        return (self.ilgis + self.plotis) * 2


rect_1 = Rectangle(5, 4)
rect_2 = Rectangle(6, 6)
print(f'Pirmo plotas: {rect_1.get_area()}, perimetras: {rect_1.get_perimeter()}')
print(f'Antro plotas: {rect_2.get_area()}, perimetras: {rect_2.get_perimeter()}')
