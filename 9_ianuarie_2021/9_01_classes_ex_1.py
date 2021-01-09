from math import pi

# ? 1. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle1 = Rectangle(5, 8)
print(rectangle1.area())



# ? 2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
# * [7:39 PM] aria cerc = pi * raza^2
# * [7:39 PM] perimetru 2*pi* raza

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


circle1 = Circle(4.8)
print(circle1.area())
print(circle1.perimeter())