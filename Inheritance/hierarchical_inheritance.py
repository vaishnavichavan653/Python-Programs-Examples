class Animal:
    def eat(self):
        print("The animal is eating.")


class Dog(Animal):
    def sound(self):
        print("The dog barks.")


class Cat(Animal):
    def sound(self):
        print("The cat meows.")


dog = Dog()
dog.eat()
dog.sound()

cat = Cat()
cat.eat()
cat.sound()
