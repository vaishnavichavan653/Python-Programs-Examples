class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_price(self):
        print(self.name, "costs", self.price)


item = Product("Notebook", 3.50)
item.show_price()
