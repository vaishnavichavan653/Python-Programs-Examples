class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_number)
        print("Marks:", self.marks)


student = Student("Anil", 12, 86)
student.show_details()
