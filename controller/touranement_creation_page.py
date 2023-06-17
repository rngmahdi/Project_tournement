import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk
import list_tournament_page
from PIL import Image
from player_page import PlayerPage

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self,container):
        super().__init__()
        # Main
        self.main = container
        self.main.columnconfigure((0,1),weight=1)
        self.main.rowconfigure(0,weight=1)
        
        self.input_frame = customtkinter.CTkFrame(self.main)
        self.input_frame.grid(row=0,column=0,sticky="news")
        
        self.img = customtkinter.CTkImage(dark_image=Image.open("./public/img/tbg.png"),size=(300,250))
        
        self.img_bg = customtkinter.CTkLabel(self.main,image=self.img,text="")
        self.img_bg.grid(row=0,column=1,sticky="news")
        
               
        self.fullName = customtkinter.CTkEntry(self.input_frame,placeholder_text="fullName")
        self.title = customtkinter.CTkEntry(self.input_frame,placeholder_text="title")
        self.type = customtkinter.CTkOptionMenu(self.input_frame, values=["LOCAL", "REGIONAL"])
        self.place = customtkinter.CTkEntry(self.input_frame,placeholder_text="place")
        self.date = customtkinter.CTkEntry(self.input_frame,placeholder_text="date")
        self.btn1 = customtkinter.CTkButton(self.input_frame,text="Ceate",command=self.createNewTournament)

        self.fullName.pack(pady=5,expand=True)
        self.title.pack(pady=5,expand=True)
        self.type.pack(pady=5,expand=True)
        self.place.pack(pady=5,expand=True)
        self.date.pack(pady=5,expand=True)
        self.btn1.pack(pady=5,expand=True)
        
    # Method      
    
    def createNewTournament(self):
        try:
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
            print("Created")
        except:
            print("Failed")


            