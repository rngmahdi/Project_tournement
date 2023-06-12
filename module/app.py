import customtkinter 
import tkinter as tk


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Main
        self.geometry(f"600x500")
        self.grid_columnconfigure((0), weight=1)
        self.title("Starting Up")
        
        # Widgets
        self.label = customtkinter.CTkLabel(self,text="Welcome to chess tournament manager")
        self.button = customtkinter.CTkButton(self,text="Create a new Account")
        
        self.label.grid(row=0,column=0,padx=20,pady=20)
        self.button.grid(row=1,column=0,padx=20,pady=10,sticky="ew")
        
        
        self.mainloop()
        
    # Methods
    
App()