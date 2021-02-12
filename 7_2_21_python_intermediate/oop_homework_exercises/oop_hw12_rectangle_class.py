
# TODO: Write a Python class named Rectangle constructed by a length and width 
# * and a method which will compute the area of a rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


if __name__ == '__main__':
    r1 = Rectangle(4, 5)
    print(r1.area())