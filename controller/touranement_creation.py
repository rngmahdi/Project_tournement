import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk
import tournament_list
from player_page import PlayerPage

class TouranementCreationPage(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Main
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=13)
        self.geometry("600x500")
        self.title("Tournament Manager")
        
        # Structure
        self.nav = customtkinter.CTkFrame(self,height=40)
        self.main = customtkinter.CTkFrame(self)
        
        # Menu
        self.route_tournament_creation = customtkinter.CTkButton(self.nav,text="+ Tournament",command=self.tournamentPage)
        self.route_tournaments_list = customtkinter.CTkButton(self.nav,text="List Tournament",command=self.listTournament)
        self.route_player = customtkinter.CTkButton(self.nav,text="Players",command=self.playersPage)
        
        # Current Active Page
        self.tournamentPage()
        
        self.nav.grid(row=0,column=0,sticky="new")
        self.main.grid(row=1,column=0,sticky="news")
        
        self.route_tournament_creation.grid(row=0,column=0,padx=5)
        self.route_tournaments_list.grid(row=0,column=1,padx=5)
        self.route_player.grid(row=0,column=2,padx=5)
        
        self.mainloop()
        
    # Methods
    def tournamentPage(self):
        
        self.cleanContainer(self.main)
        
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
        
    def listTournament(self):
        self.cleanContainer(self.main)
        tournament_list.TournamentList(self.main)
    
    def playersPage(self):
        self.cleanContainer(self.main)
        PlayerPage(self.main)
    
        
        
        
    # 
    # 
    # 
    # 
    # 
    # 
    
        
    
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
    
    
            
            
    
    
    
    
            
            
    
    
    def destroy(self):
        return self.quit()

    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()
            
TouranementCreationPage()