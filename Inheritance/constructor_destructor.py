class Student:
    def __init__(self, name):
        self.name = name
        print(self.name, "object created")

    def show_name(self):
        print("Student name:", self.name)

    def __del__(self):
        print(self.name, "object destroyed")


student = Student("Asha")
student.show_name()
del student
