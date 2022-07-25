from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Popup open")
root.geometry = "200x100"

def askuser():
    res = messagebox.askquestion("Dear User", "Have you used this program before?")
    if res == "no":
        messagebox.showinfo("Instructions", "Instructions go here.")
    else:
        messagebox.showinfo("Enjoy", "Cool, enjoy using the program.")

askuser()
root.mainloop()