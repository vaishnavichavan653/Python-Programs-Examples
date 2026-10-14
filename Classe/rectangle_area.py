class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def show_area(self):
        print("Area:", self.length * self.width)


shape = Rectangle(8, 5)
shape.show_area()
