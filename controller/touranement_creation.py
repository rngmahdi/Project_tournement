import customtkinter 
import sqlite3
import tkinter as tk
from player import Player


class TouranementCreationPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Main
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=13)
            
        self.title("Create a new Tourenement")
        self.geometry("600x500")
        
        self.nav = customtkinter.CTkFrame(self,height=40)
        self.main = customtkinter.CTkFrame(self)
        
        #* Routes
        self.route_tournament_creation = customtkinter.CTkButton(self.nav,text="+ Tournament")
        self.route_tournaments_list = customtkinter.CTkButton(self.nav,text="List Tournament")
        self.route_player = customtkinter.CTkButton(self.nav,text="Players")
        
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
        
        self.route_tournament_creation.grid(row=0,column=0)
        self.route_tournaments_list.grid(row=0,column=1)
        self.route_player.grid(row=0,column=2)
        
        self.nav.grid(row=0,column=0,sticky="new")
        self.main.grid(row=1,column=0,sticky="news")
        
        self.mainloop()
        
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
        Player(self)
    
    def destroy(self):
        return self.quit()
    
TouranementCreationPage()