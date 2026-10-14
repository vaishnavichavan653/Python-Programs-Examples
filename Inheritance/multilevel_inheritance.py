class Person:
    def show_person(self):
        print("I am a person.")


class Student(Person):
    def study(self):
        print("I am studying.")


class GraduateStudent(Student):
    def research(self):
        print("I am doing research.")


student = GraduateStudent()
student.show_person()
student.study()
student.research()
