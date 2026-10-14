class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


first = Vector(2, 3)
second = Vector(4, 5)

print("First vector:", first)
print("Second vector:", second)
print("Sum:", first + second)
