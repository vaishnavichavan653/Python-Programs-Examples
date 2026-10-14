class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def show_course(self):
        print(self.name, "studies Python.")


class Worker(Person):
    def show_department(self):
        print(self.name, "works in the IT department.")


class TeachingAssistant(Student, Worker):
    def __init__(self, name):
        Person.__init__(self, name)


assistant = TeachingAssistant("Ravi")
assistant.show_course()
assistant.show_department()
