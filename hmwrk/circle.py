import math


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return round((math.pi * (self.radius ** 2)), 2)

    def circumference(self):
        return round((2 * math.pi * self.radius), 2)


circle_1 = Circle(5)
print(f'The area of circle of radius of {circle_1.radius} is {circle_1.area()}'
      f', circumference - {circle_1.circumference()}.')
