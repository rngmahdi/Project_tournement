from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image
import sqlite3
from match_page import MatchPage
from message_box import MessageBox
from players_in_tournament_page import PlayerInTournament
# import container


class TournamentList(customtkinter.CTk):
    def __init__(self, container):
        super().__init__()
        self.main = container
        self.frame = customtkinter.CTkScrollableFrame(self.main, width=700, height=container.winfo_height()-100)
        self.frame.pack()
        self.getAllTournaments()
        # print(container.winfo_height())
        # data = getTournamentData()

    def getAllTournaments(self):
        self.cleanContainer(self.frame)
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()
            data = cursor.execute("SELECT * FROM tournament").fetchall()
            connect.commit()
            connect.close()
            
            if (len(data) != 0):
                for i in range(len(data)):
                    #   print(data)
                    self.div = customtkinter.CTkFrame(self.frame)
                    self.div.pack(padx=10, pady=10)
                    #! tournament title
                    self.tournament_title_label = customtkinter.CTkLabel(
                        self.div, text="Tournament's title :")
                    self.tournament_title_label.grid(row=0, column=0)
                    self.tournament_title_data = StringVar(value=data[i][1])
                    self.tournament_title = customtkinter.CTkLabel(
                        self.div, textvariable=self.tournament_title_data)
                    self.tournament_title.grid(row=0, column=1, padx=20)
                    #! tournament's place
                    self.tournament_place_label = customtkinter.CTkLabel(
                        self.div, text="Place :")
                    self.tournament_place_label.grid(row=1, column=0)
                    self.tournament_place_data = StringVar(value=data[i][2])
                    self.tournament_place = customtkinter.CTkLabel(
                        self.div, textvariable=self.tournament_place_data)
                    self.tournament_place.grid(row=1, column=1)
                    #! Tournament Date
                    self.tournament_date_label = customtkinter.CTkLabel(
                        self.div, text="Date")
                    self.tournament_date_label.grid(row=2, column=0)
                    self.tournament_date_data = StringVar(value=data[i][3])
                    self.tournament_date = customtkinter.CTkLabel(
                        self.div, textvariable=self.tournament_date_data)
                    self.tournament_date.grid(row=2, column=1)
                    #! tournament creator's Name
                    self.tournament_creator_label = customtkinter.CTkLabel(
                        self.div, text="Creator")
                    self.tournament_creator_label.grid(row=3, column=0)
                    self.tournament_creator_data = StringVar(value=data[i][4])
                    self.tournament_creator = customtkinter.CTkLabel(
                        self.div, textvariable=self.tournament_creator_data)
                    self.tournament_creator.grid(row=3, column=1)
                    #! Tournament Type
                    self.tournament_type_label = customtkinter.CTkLabel(
                        self.div, text="Tournament's Type")
                    self.tournament_type_label.grid(row=4, column=0)
                    self.tournament_type_data = StringVar(value=data[i][5])
                    self.tournament_type = customtkinter.CTkLabel(
                        self.div, textvariable=self.tournament_type_data)
                    self.tournament_type.grid(row=4, column=1)
                    #! Actions
                    self.action_label = customtkinter.CTkLabel(
                        self.div, text="Actions :")
                    self.action_label.grid(row=5, column=0)
                    self.actions = customtkinter.CTkFrame(self.div, height=30)
                    self.actions.grid(row=5, column=1)
                    self.removeBtn = customtkinter.CTkButton(
                        self.actions, text="Remove", command=lambda idtournament=data[i][0]: self.removeTournament(idtournament))
                    self.removeBtn.grid(row=0, column=0)
                    # self.updateBtn = customtkinter.CTkButton(self.actions, text="Edit")
                    self.idtournament = self.tournament_title_data.get()

                    self.optionSelected = StringVar()
                    self.updateBtn = customtkinter.CTkOptionMenu(self.actions, values=[
                        "Players", "Edit Tournament", "Matches"], command=lambda choice=self.optionSelected, id=data[i][0]: self.optionMenu(choice, id,self.main), variable=self.optionSelected)
                    self.updateBtn.set("Update")
                    # print(idtournament)
                    self.updateBtn.grid(row=0, column=1)
        except:
            return False


    def getSpecificTournament(self,idTournament):
        connect = sqlite3.connect("./database/database.db")
        cursor = connect.cursor()
        tournament = cursor.execute(
            f"SELECT * FROM tournament where id = ?", (idTournament,)).fetchone()
        connect.commit()
        connect.close()
        return tournament


    def updateTournament(self,idTournament):
        data = self.getSpecificTournament(idTournament)
        # print(data)
        window = customtkinter.CTkToplevel(self.main)
        window.title("Update tournament")
        window.geometry("600x500")
        window.attributes('-topmost', 'true')
        window.columnconfigure((0, 1), weight=1)
        window.rowconfigure(0, weight=1)

        input_frame = customtkinter.CTkFrame(window)
        input_frame.grid(row=0, column=0, sticky="news")

        img = customtkinter.CTkImage(dark_image=Image.open("./public/img/tbg.png"), size=(300, 250))

        img_bg = customtkinter.CTkLabel(window, image=img, text="")
        img_bg.grid(row=0, column=1, sticky="news")

        fullName = customtkinter.CTkEntry(input_frame, placeholder_text="fullName")
        title = customtkinter.CTkEntry(input_frame, placeholder_text="title")
        type = customtkinter.CTkOptionMenu(
            input_frame, values=["LOCAL", "REGIONAL"])
        place = customtkinter.CTkEntry(input_frame, placeholder_text="place")
        date = customtkinter.CTkEntry(input_frame, placeholder_text="date")
        btn1 = customtkinter.CTkButton(input_frame, text="update", command=lambda id=idTournament, fullname=fullName,
                                       title=title, type=type, place=place, date=date: self.updateInfos(id, fullname, title, type, place, date))

        fullName.insert(customtkinter.END, data[4])
        title.insert(customtkinter.END, data[1])
        type.set(data[5])
        place.insert(customtkinter.END, data[2])
        date.insert(customtkinter.END, data[3])
        #
        fullName.pack(pady=5, expand=True)
        title.pack(pady=5, expand=True)
        type.pack(pady=5, expand=True)
        place.pack(pady=5, expand=True)
        date.pack(pady=5, expand=True)
        btn1.pack(pady=5, expand=True)


    def updateInfos(self,id, fullname, title, type, place, date):
        fulnameNew = fullname.get()
        titleNew = title.get()
        typeNew = type.get()
        placeNew = place.get()
        dateNew = date.get()
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()
            cursor.execute("UPDATE tournament SET title = ? , place = ? , date = ? , name_of_creator = ? , type = ? WHERE id = ? ",
                        (titleNew, placeNew, dateNew, fulnameNew, typeNew, id))
            connect.commit()
            connect.close()
        except:
            print("error")
        self.quit()
        self.getAllTournaments()


    def removeTournament(self, id):
        # print(id)
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("DELETE FROM  tournament WHERE id = ? ", (id,))

            connect.commit()
            connect.close()
            MessageBox(self.main, "The Tournament is Deleted", "success")
            self.getAllTournaments()
        except:
            MessageBox(self.main, "Failed to delete the tournament", "error")

    def matchPage(self,id):
        MatchPage()
        # redirect to match page

    def playerInTournamentPage(self,id):
        PlayerInTournament(self.main)

    def optionMenu(self,choice, id, container):
        if (choice == "Edit Tournament"):
            self.updateTournament(id)
        elif(choice == "Matches"):
            self.matchPage(id)
        elif (choice == "Players"):
            self.playerInTournamentPage(id)
        # print(f"choice : {choice}")
        # print(f"id {id}")

    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()
