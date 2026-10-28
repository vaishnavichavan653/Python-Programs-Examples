from tkinter import *

root = Tk()
root.title("Message Example")
root.geometry("300x200")

msg = Message(root, text="Welcome to Python GUI Programming!")
msg.pack()

root.mainloop()