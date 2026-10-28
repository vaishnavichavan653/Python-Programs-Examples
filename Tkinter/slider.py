from tkinter import *

root = Tk()
root.title("Scale Example")
root.geometry("300x200")

scale = Scale(root, from_=0, to=100)
scale.pack()

root.mainloop()