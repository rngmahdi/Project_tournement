import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk
import list_tournament_page
from player_page import PlayerPage

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self,container):
        super().__init__()
        # Main
        self.main = container
        
        self.fullName = customtkinter.CTkEntry(self.main,placeholder_text="fullName")
        self.title = customtkinter.CTkEntry(self.main,placeholder_text="title")
        self.type = customtkinter.CTkOptionMenu(self.main, values=["LOCAL", "REGIONAL"])
        self.place = customtkinter.CTkEntry(self.main,placeholder_text="place")
        self.date = customtkinter.CTkEntry(self.main,placeholder_text="date")
        self.btn1 = customtkinter.CTkButton(self.main,text="Ceate",command=self.createNewTournament)

        self.fullName.grid()
        self.title.grid()
        self.type.grid()
        self.place.grid()
        self.date.grid()
        self.btn1.grid()
        
    # Methods
        
        
        
    def listTournament(self):
        self.cleanContainer(self.main)
        list_tournament_page.TournamentList(self.main)
    
    def playersPage(self):
        self.cleanContainer(self.main)
        PlayerPage(self.main)
        
    
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


            