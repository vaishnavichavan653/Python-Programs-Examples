class Flyer:
    def fly(self):
        print("The duck can fly.")


class Swimmer:
    def swim(self):
        print("The duck can swim.")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
duck.swim()
