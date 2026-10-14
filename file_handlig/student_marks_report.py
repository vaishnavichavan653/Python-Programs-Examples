import csv

students = [
    ["RollNo", "Name", "Marks"],
    [101, "Amit", 85],
    [102, "Priya", 92],
    [103, "Rahul", 78],
]

with open("student_records.csv", "w", newline="") as file:
    csv.writer(file).writerows(students)

with open("student_records.csv", "r") as file:
    records = list(csv.DictReader(file))

for student in records:
    print(student["RollNo"], student["Name"], student["Marks"])

top_student = max(records, key=lambda student: int(student["Marks"]))
average = sum(int(student["Marks"]) for student in records) / len(records)

print("Highest marks:", top_student["Name"], top_student["Marks"])
print("Average marks:", average)
print("Students scoring above 80:")
for student in records:
    if int(student["Marks"]) > 80:
        print(student["Name"])
