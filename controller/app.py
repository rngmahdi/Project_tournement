import customtkinter
import tkinter as tk
from PIL import Image
from touranement_creation import TouranementCreationPage
from model.window import Window



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.window = Window("Start Up","600x400")
        # Main
        self.window.rowconfigure(0,weight=2)
        self.window.rowconfigure(1,weight=1)
        self.window.columnconfigure(0,weight=1)
        self.img = customtkinter.CTkImage(dark_image=Image.open("./public/img/bg.png"),size=(600,250))
        
        # Widgets
        self.frame_1 = customtkinter.CTkLabel(self,image=self.img,text="")
        self.button = customtkinter.CTkButton(self,text="Create a new Account",command=self.start,fg_color="#6C63FF")
        
        # self.label.grid(row=1,column=0)
        self.frame_1.grid(row=0,column=0,sticky="ewns",padx=10,pady=10)
        self.button.grid(row=1,column=0)
        
    # Methods
    def start(self):
        TouranementCreationPage(self)
    
    def destroy(self):
        return self.quit()
    
App()