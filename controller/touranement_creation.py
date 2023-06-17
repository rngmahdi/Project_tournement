import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk
import tournament_list


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
        
        self.addPlayer_frame = customtkinter.CTkFrame(self.main,width=600)
        self.listPlayer_frame = customtkinter.CTkFrame(self.main,width=600)
        
        self.fullName = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="fullName")
        self.rating = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="rating")
        self.phone = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="phone")
        self.email = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="email")
        self.btn1 = customtkinter.CTkButton(self.main,text="Add PLayer",command=self.addPlayer)
        
        # self.tree = ttk.Treeview(self.listPlayer_frame, columns=('id','fullName', 'rating','phone' ,'email','tournamentId'), show='headings')
        # self.tree.heading('id', text='id')
        # self.tree.heading('fullName', text='Full Name')
        # self.tree.heading('rating', text='Rating')
        # self.tree.heading('phone', text='Phone')
        # self.tree.heading('email', text='Email')
        # self.tree.heading('tournamentId', text='Tour Id')
        
        # # print(self.getAllPlayers())
        # for elem in self.getAllPlayers():
        #     self.tree.insert('', tk.END, values=elem)
        
        for player in self.getAllPlayers():
            fullName = player[1]
            rating = player[2]
            phone = player[3]
            email = player[4]
            player_frame = customtkinter.CTkFrame(self.listPlayer_frame)
            player_frame.grid()
            customtkinter.CTkLabel(player_frame,text=fullName).grid()
            customtkinter.CTkButton(player_frame,text="Edit").grid()
            
        
        self.fullName.grid()
        self.rating.grid()
        self.phone.grid()
        self.email.grid()
        
        self.addPlayer_frame.grid(column=0,sticky="news")
        self.btn1.grid(pady=10)
        self.listPlayer_frame.grid(column=0,sticky="news")
        
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
    
    def addPlayer(self):
        try:
            fullName = self.fullName.get()
            phone = self.phone.get()
            email = self.email.get()
            rating = self.rating.get()
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("INSERT INTO player (fullname,rating,phone,email) VALUES (?,?,?,?)",(fullName,phone,email,rating))
            connect.commit()
            connect.close()
            print("Player Addes")
        except:
            print("Failed to Add Player")
            
    def getAllPlayers(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            data = cursor.execute("SELECT * FROM player").fetchall()
            connect.commit()
            connect.close()
            return data
        except:
            return False
    
    def destroy(self):
        return self.quit()

    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()
            
TouranementCreationPage()