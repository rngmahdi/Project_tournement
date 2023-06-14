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
        
        self.frame_1 = customtkinter.CTkFrame(window,height=100,width=200)
        self.firstName = customtkinter.CTkEntry(self.frame_1,placeholder_text="firstName")
        self.lastName = customtkinter.CTkEntry(self.frame_1,placeholder_text="lastName")
        self.birthDay = customtkinter.CTkEntry(self.frame_1,placeholder_text="birthDay")
        self.email = customtkinter.CTkEntry(self.frame_1,placeholder_text="email")
        
        self.frame_2 = customtkinter.CTkFrame(window,height=100,width=200)
        self.title = customtkinter.CTkEntry(self.frame_2,placeholder_text="title")
        self.type = customtkinter.CTkEntry(self.frame_2,placeholder_text="type")
        self.rounds = customtkinter.CTkEntry(self.frame_2,placeholder_text="rounds")
        self.place = customtkinter.CTkEntry(self.frame_2,placeholder_text="place")
        self.startingDate = customtkinter.CTkEntry(self.frame_2,placeholder_text="startingDate")
        self.endingDate = customtkinter.CTkEntry(self.frame_2,placeholder_text="endtingDate")
        
        self.frame_3 = customtkinter.CTkFrame(window,height=100,width=200)
        self.btn1 = customtkinter.CTkButton(self.frame_3,text="Ceate")
        self.btn2 = customtkinter.CTkButton(self.frame_3,text="Cancel")

        self.frame_1.grid()
        self.firstName.grid()
        self.lastName.grid()
        self.birthDay.grid()
        self.email.grid()
        
        self.frame_2.grid()
        self.title.grid()
        self.type.grid()
        self.rounds.grid()
        self.place.grid()
        self.startingDate.grid()
        self.endingDate.grid()
        
        
        self.frame_3.grid()
        self.btn1.grid()
        self.btn2.grid()
        
        
    # Methods
    def createNewTournament(self):
        
        firstName = self.firstName.get()
        lastName = self.lastName.get()
        birthDay = self.birthDay.get()
        email = self.email.get()
        title = self.title.get()
        type = self.type.get()
        rounds = self.rounds.get()
        place = self.place.get()
        startingDate = self.startingDate.get()
        endingDate = self.endingDate.get()