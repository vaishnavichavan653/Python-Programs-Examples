class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calculator = Calculator()
print("Sum:", calculator.add(12, 4))
print("Difference:", calculator.subtract(12, 4))
