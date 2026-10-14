class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Car brand:", self.brand)


my_car = Car("Toyota")
my_car.show_brand()
