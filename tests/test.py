from tkinter import *
from tkinter import ttk
import test2

root = Tk()
root.geometry("700x800")
root.title("Home Page")
def redirect():
   windon= test2.Window(root)
   
btn = Button(root,text="Click here !",command=redirect)
btn.grid(row=1,column=1)
root.mainloop()