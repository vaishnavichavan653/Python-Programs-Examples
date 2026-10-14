class Person:
    def __init__(self, name):
        self.__name = name

    def __show_name(self):
        print("Name:", self.__name)

    def show_private_details(self):
        self.__show_name()


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self._salary = salary

    def _show_salary(self):
        print("Salary:", self._salary)


class Manager(Employee):
    def show_details(self):
        self.show_private_details()
        self._show_salary()


manager = Manager("Meera", 50000)
manager.show_details()
