from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_area(shape):
    print(f"Area: {shape.area():.2f}")


print_area(Circle(3))
print_area(Rectangle(4, 5))
