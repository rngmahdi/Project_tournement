import customtkinter 
import sqlite3
import tkinter as tk
from route import Route

class TouranementCreationPage(customtkinter.CTk,Route):
    def __init__(self,window):
        super().__init__()
        
        # Main
        for child in window.winfo_children():
            child.destroy()
            
        window.title("Create a new Tourenement")
        
        # Widgets
        
        self.frame_1 = customtkinter.CTkFrame(window,height=100,width=200)
        self.fullName = customtkinter.CTkEntry(self.frame_1,placeholder_text="fullName")
        
        self.frame_2 = customtkinter.CTkFrame(window,height=100,width=200)
        self.title = customtkinter.CTkEntry(self.frame_2,placeholder_text="title")
        self.type = customtkinter.CTkEntry(self.frame_2,placeholder_text="type")
        self.place = customtkinter.CTkEntry(self.frame_2,placeholder_text="place")
        self.date = customtkinter.CTkEntry(self.frame_2,placeholder_text="startingDate")
        
        self.frame_3 = customtkinter.CTkFrame(window,height=100,width=200)
        self.btn1 = customtkinter.CTkButton(self.frame_3,text="Ceate")
        self.btn2 = customtkinter.CTkButton(self.frame_3,text="Cancel")

        self.frame_1.grid()
        self.fullName.grid()
        
        self.frame_2.grid()
        self.title.grid()
        self.type.grid()
        self.place.grid()
        self.date.grid()
        
        
        self.frame_3.grid()
        self.btn1.grid()
        self.btn2.grid()
        
        
    # Methods
    def createNewTournament(self):
        
        fullName = self.fullName.get()
        title = self.title.get()
        type = self.type.get()
        place = self.place.get()
        date = self.date.get()
        

        connect = sqlite3.connect("./database/database.db")
        cursor = connect.cursor()

        cursor.execute("INSERT INTO db_tournament VALUES (title,place,date,name_of_creator,type)",(title,place,date,fullName,type))
        connect.commit()
        connect.close()
    
    def destroy(self):
        return super().destroy()