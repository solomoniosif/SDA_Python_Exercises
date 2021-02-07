from oop_abstract_classes import Figure
from dataclasses import dataclass

@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def perimeter(self):
        return 2 * (self.b + self.a)

    def  area(self):
        return self.a * self.b


# * Check the __init__, __repr__ and __eq__ provided by dataclass decorator

rectangle1 = Rectangle(3,3)

rectangle2 = Rectangle(3,3)

print(rectangle1 is rectangle2)

print(rectangle2 == rectangle1)

print(rectangle1)
