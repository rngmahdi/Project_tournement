
import customtkinter
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from model.match import Match
from model.database import DataBase

class MatchPage(customtkinter.CTk):
    def __init__(self,container,id):
        super().__init__()
        self.main = container
        self.selectedTournamentId = id
        self.topLevel = customtkinter.CTkToplevel(self.main)
        self.topLevel.geometry("600x500")
        self.topLevel.title("")
        self.topLevel.attributes('-topmost', 'true')
        self.topLevel.columnconfigure(0,weight=1)
        self.topLevel.rowconfigure(1,weight=1)
        
        # Widgets
        self.nav = customtkinter.CTkFrame(self.topLevel,height=40)
        self.nav.grid(row=0,column=0,sticky="ew")
        self.viewer = customtkinter.CTkFrame(self.topLevel)
        self.viewer.grid(row=1,column=0,sticky="news")
        
        self.btn_generate = customtkinter.CTkButton(self.nav,text="Generate Matches",command=self.generateMatches)
        self.btn_generate.grid(padx=2,pady=2)
        # 
        
    def generateMatches(self):
        # get all players
        databaseController = DataBase("./database/database.db")
        allMatches = databaseController.customQuery("SELECT * FROM match WHERE tournamentId = ?;",(self.selectedTournamentId,))
        allPlayers = databaseController.customQuery("SELECT * FROM player WHERE tournamentId = ?;",(self.selectedTournamentId,))
        print(allPlayers)
        
        # see if valid
        if not(len(allPlayers) % 2) or len(allMatches) > 0 or len(allPlayers) == 0:
            # Matches are generated
            print("didn't work")            
        else:
            # generate matches
            print("didn't work")            
            # generate match and save
            for player1 in allPlayers:
                for i in range(0,len(allPlayers)):
                    if(player1 == allPlayers[i]):
                        continue
                    else:
                        # customtkinter.CTkLabel(self.viewer,text=f"{player1}Vs{player2}")
                        Match(player1[0],allPlayers[i][0],0,0,i,0,self.selectedTournamentId).add() # Status 1=complete 0=inprogress 2=cancel
                                                
        # block generating and adding any more players