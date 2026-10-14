class Circle:
    def __init__(self, radius):
        self.radius = radius

    def show_area(self):
        print("Area:", 3.14 * self.radius * self.radius)


circle = Circle(5)
circle.show_area()
