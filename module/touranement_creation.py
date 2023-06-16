import customtkinter 
import sqlite3
import tkinter as tk
from player import Player

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self,window):
        super().__init__()
        # Main
        self.window = window
        for child in self.window.winfo_children():
            child.destroy()
            
        self.window.title("Create a new Tourenement")
        
        # Widgets
        
        self.frame_1 = customtkinter.CTkFrame(window,height=100,width=200)
        self.fullName = customtkinter.CTkEntry(self.frame_1,placeholder_text="fullName")
        
        self.frame_2 = customtkinter.CTkFrame(window,height=100,width=200)
        self.title = customtkinter.CTkEntry(self.frame_2,placeholder_text="title")
        self.type = customtkinter.CTkEntry(self.frame_2,placeholder_text="type")
        self.place = customtkinter.CTkEntry(self.frame_2,placeholder_text="place")
        self.date = customtkinter.CTkEntry(self.frame_2,placeholder_text="startingDate")
        
        self.frame_3 = customtkinter.CTkFrame(window,height=100,width=200)
        self.btn1 = customtkinter.CTkButton(self.frame_3,text="Ceate",command=self.createNewTournament)
        self.btn2 = customtkinter.CTkButton(self.frame_3,text="Cancel",command=self.player)

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

        cursor.execute("INSERT INTO dbtournament (title,place,date,name_of_creator,type) VALUES (?,?,?,?,?)",(title,place,date,fullName,type))
        connect.commit()
        connect.close()
        
    def player(self):
        Player(self.window)
    