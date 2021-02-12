
# TODO: Write a Python class named Circle constructed by a radius 
# * and two methods which will compute the area and the perimeter of a circle.
 
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    c1 = Circle(4)

    print(c1.area())
    print(c1.perimeter())