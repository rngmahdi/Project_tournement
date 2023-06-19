import customtkinter 
import list_tournament_page #Function
from list_tournament_page2 import TournamentList # Class
from player_page import PlayerPage #class
from touranement_creation_page import TouranementCreationPage #class
from PIL import Image
from message_box import MessageBox
customtkinter.set_default_color_theme("config/custom_theme.json")


class Root(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()
        # Main
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=13)
        self.geometry("600x500")
        self.title("Tournament Manager")
        self.iconbitmap("./public/img/icon_edit.ico")
        
        
        # Structure
        self.nav = customtkinter.CTkFrame(self,height=40)
        self.main = customtkinter.CTkFrame(self)
        
        self.img = customtkinter.CTkImage(dark_image=Image.open("./public/img/icon_edit.png"),size=(15,15))
        # Menu 
        self.route_tournament_creation = customtkinter.CTkButton(self.nav,image=self.img,text="Tournament",command=self.tournamentCreationPage)
        self.route_tournaments_list = customtkinter.CTkButton(self.nav,text="List Tournament",command=self.listTournamentPage)
        self.route_player = customtkinter.CTkButton(self.nav,text="Players",command=self.playerPage)
        
        # Current Active Page
        self.tournamentCreationPage()
        
        self.nav.grid(row=0,column=0,sticky="new")
        self.main.grid(row=1,column=0,sticky="news")
        
        self.route_tournament_creation.grid(row=0,column=0,padx=5)
        self.route_tournaments_list.grid(row=0,column=1,padx=5)
        self.route_player.grid(row=0,column=2,padx=5)
        
        
        self.mainloop()
        
    # Methods
    def tournamentCreationPage(self):
        self.cleanContainer(self.main)
        TouranementCreationPage(self.main)
    
    def listTournamentPage(self):
        self.cleanContainer(self.main)
        # list_tournament_page.TournamentList(self.main)
        TournamentList(self.main)
    
    def playerPage(self):
        self.cleanContainer(self.main)
        PlayerPage(self.main)

    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()
            
    def destroy(self):
        return self.quit()
Root()