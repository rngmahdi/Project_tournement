import customtkinter 
import list_tournament_page #Function
from player_page import PlayerPage #class
from touranement_creation_page import TouranementCreationPage #class

class Root(customtkinter.CTk):
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
        self.route_tournaments_list = customtkinter.CTkButton(self.nav,text="List Tournament",command=self.listTournamentPage)
        self.route_player = customtkinter.CTkButton(self.nav,text="Players",command=self.playerPage)
        
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
        TouranementCreationPage(self.main)
             
    def listTournamentPage(self):
        self.cleanContainer(self.main)
        list_tournament_page.TournamentList(self.main)
    
    def playerPage(self):
        self.cleanContainer(self.main)
        PlayerPage(self.main)

    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()
            
    def destroy(self):
        return self.quit()
Root()