import customtkinter 
import tkinter as tk

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self,window):
        super().__init__()
        
        # Main
        for child in window.winfo_children():
            child.destroy()
            
        window.title("Create a new Tourenement")

        # Widgets
        customtkinter.CTkOptionMenu(window, values=["option 1", "option 2"])
        
    