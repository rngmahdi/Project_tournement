import customtkinter
from tkinter import *
import sqlite3

class PlayerInTournament(customtkinter.CTk):
    def __init__(self, container):
        super().__init__()
        self.main = container
        self.frame = customtkinter.CTkToplevel(self.main)
        self.frame.geometry("600x500")
        self.frame.attributes('-topmost', 'true')
        self.playerJoined = customtkinter.CTkFrame(self.frame)
        self.playerJoined.pack(padx=50,pady=30)
        self.playerJoinedHeader = customtkinter.CTkFrame(self.playerJoined)
        self.playerJoinedHeader.pack(padx=50)
        self.label = customtkinter.CTkLabel(self.playerJoinedHeader, text="Players in Touenament")
        self.label.pack(padx=50)
        self.playersListContainer = customtkinter.CTkFrame(self.frame)
        self.playersListContainer.pack()
        
        self.getPlayersJoined()

    def getPlayersJoined(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()
            data = cursor.execute("SELECT * FROM player WHERE tournamentId = 25").fetchall()
            self.players = cursor.execute("SELECT * FROM player").fetchall()
            # if (len(data) == 0):
            #     print("no players")
            # print(players)
            connect.commit()
            connect.close()
            # print(self.players)
            for i in self.players :
                self.div = customtkinter.CTkFrame(self.playersListContainer)
                fullname = StringVar(self.div,i[1])
                self.playerName = customtkinter.CTkLabel(self.div,textvariable=fullname)
                self.playerName.grid(row=0,column=0)
                rating = StringVar(self.div,f"rating {i[2]}")
                self.playerRating = customtkinter.CTkLabel(self.div,textvariable=rating)
                self.playerRating.grid(row=0,column=1,padx=10)
                print("1")
                self.div.pack(pady=4)
                print("2")

        except:
            print("error")

    def getAllPlayers(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cusror = connect.cursor()
            data = cursor.execute("SELECT * FROM player").fetchall()
            connect.close()
            return data
        except:
            return False