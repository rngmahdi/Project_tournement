from tkinter import * 
from tkinter import font
from tkinter.font import Font
from tkinter import ttk
import customtkinter

root = Tk()
root.title("Tournament manegements")
root.state("zoomed")
root.geometry("600x700")
# root.update_idletasks() 
########################################################################
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

buttonFont = Font(family="Tekton Pro",
                 size=40,
                 weight="bold",
                       )

button = customtkinter.CTkButton(root, text="Create new tournament",
                                 font=("Bahnschrift Light Condensed",40,"bold"))
button.configure(fg_color="#37CEFE",width=400,height=80)
button.pack(pady=20,padx=20)
button.place(x=(width/2)-200 ,y=height/2)

root.mainloop()