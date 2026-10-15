import matplotlib.pyplot as plt

students = ["Amit", "Priya", "Rahul", "Sneha"]
marks = [80, 90, 75, 85]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()