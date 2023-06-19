import customtkinter
import sqlite3

class PlayerInTournament(customtkinter.CTk):
    def __init__(self, container):
        super().__init__()
        self.main = container
        self.frame = customtkinter.CTkToplevel(self.main)
        self.frame.geometry("600x500")
        self.frame.attributes('-topmost', 'true')
        self.playerJoined = customtkinter.CTkFrame(self.frame)
        self.playerJoined.pack(padx=50)
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
            data = cursor.execute("SELECT * FROM player WHERE tournamentId = 24").fetchall()
            if (len(data) == 0):
                print("no players")
            connect.commit()
            connect.close()
            for i in range(len(data)):
                players = self.getAllplayers()
                fullname = StringVar(players[i][1])
                print(fullname)
                self.div = customtkinter.CTkFrame(self.playersListContainer)
                self.playerName = customtkinter.CTkLabel(self.div,textvariable=fullname)
                self.playerName.pack()
                self.div.pack()
        except:
            return False

    def getAllPlayers(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cusror = connect.cursor()
            data = cursor.execute("SELECT * FROM player").fetchall()
            connect.close()
            return data
        except:
            return False