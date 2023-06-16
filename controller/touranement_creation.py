import customtkinter 
import sqlite3
import tkinter as tk
from player import Player

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self,window):
        super().__init__()
        # Main
        self.window = window
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0,weight=1)
        
        for child in self.window.winfo_children():
            child.destroy()
            
        self.window.title("Create a new Tourenement")
        
        # Widgets
        
        self.input_frame = customtkinter.CTkFrame(self.window,fg_color="yellow")
        self.bg_frame = customtkinter.CTkFrame(self.window)
        
        self.frame_1 = customtkinter.CTkFrame(self.window,height=100,width=200)
        self.fullName = customtkinter.CTkEntry(self.frame_1,placeholder_text="fullName")
        
        self.frame_2 = customtkinter.CTkFrame(self.window,height=100,width=200)
        self.title = customtkinter.CTkEntry(self.frame_2,placeholder_text="title")
        self.type = customtkinter.CTkEntry(self.frame_2,placeholder_text="type") 
        self.place = customtkinter.CTkEntry(self.frame_2,placeholder_text="place")
        self.date = customtkinter.CTkEntry(self.frame_2,placeholder_text="date")
        
        self.frame_3 = customtkinter.CTkFrame(self.window,height=100,width=200)
        self.btn1 = customtkinter.CTkButton(self.frame_3,text="Ceate",command=self.createNewTournament)
        self.btn2 = customtkinter.CTkButton(self.frame_3,text="Cancel",command=self.player)

        self.input_frame.grid(column=0,row=0,sticky="ewns")
        self.bg_frame.grid(column=1,row=0,sticky="ewns")
        
    # Methods
    def createNewTournament(self):
        
        fullName = self.fullName.get()
        title = self.title.get()
        type = self.type.get()
        place = self.place.get()
        date = self.date.get()
        

        connect = sqlite3.connect("./database/database.db")
        cursor = connect.cursor()

        cursor.execute("INSERT INTO tournament (title,place,date,name_of_creator,type) VALUES (?,?,?,?,?)",(title,place,date,fullName,type))
        connect.commit()
        connect.close()
        
    def player(self):
        Player(self.window)
    