import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "HTML"]
marks = [40, 30, 20, 10]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")

plt.title("Subject Distribution")

plt.show()