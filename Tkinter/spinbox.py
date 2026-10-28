from tkinter import *

root = Tk()
root.title("Spinbox Example")
root.geometry("300x200")

spin = Spinbox(root, from_=1, to=10)
spin.pack()

root.mainloop()