
# ! #########################################################################
# ! ####################       ABSTRACT CLASSES       #######################
# ! #########################################################################

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 4
    
    def area(self):
        return self.side ** 2

    def __repr__(self):
        return f"Square({self.side})"

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b

    def __repr__(self):
        return f"Rectangle({self.side_a},{self.side_b})"


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * self.radius * pi

    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return f"Circle({self.radius})"


if __name__ == '__main__':
    figures = [Square(7), Rectangle(4, 6), Circle(4)]

    for fig in figures:
        print(f"\n{fig} has the perimeter {round(fig.perimeter(), 2)}, and area {round(fig.area(), 2)}.")
    print()