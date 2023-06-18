from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image
import sqlite3
from match_page import window
from message_box import MessageBox
# import root


def TournamentList(root):
    frame = customtkinter.CTkScrollableFrame(
        root, width=700, height=root.winfo_height()-100)
    frame.pack()
    # print(root.winfo_height())
    data = getTournamentData()
    if (len(data) != 0):
        for i in range(len(data)):
            pass
            #   print(data)
            div = customtkinter.CTkFrame(frame)
            div.pack(padx=10, pady=10)
            #! tournament title
            tournament_title_label = customtkinter.CTkLabel(
                div, text="Tournament's title :")
            tournament_title_label.grid(row=0, column=0)
            tournament_title_data = StringVar(value=data[i][1])
            tournament_title = customtkinter.CTkLabel(
                div, textvariable=tournament_title_data)
            tournament_title.grid(row=0, column=1, padx=20)
            #! tournament's place
            tournament_place_label = customtkinter.CTkLabel(
                div, text="Place :")
            tournament_place_label.grid(row=1, column=0)
            tournament_place_data = StringVar(value=data[i][2])
            tournament_place = customtkinter.CTkLabel(
                div, textvariable=tournament_place_data)
            tournament_place.grid(row=1, column=1)
            #! Tournament Date
            tournament_date_label = customtkinter.CTkLabel(div, text="Date")
            tournament_date_label.grid(row=2, column=0)
            tournament_date_data = StringVar(value=data[i][3])
            tournament_date = customtkinter.CTkLabel(
                div, textvariable=tournament_date_data)
            tournament_date.grid(row=2, column=1)
            #! tournament creator's Name
            tournament_creator_label = customtkinter.CTkLabel(
                div, text="Creator")
            tournament_creator_label.grid(row=3, column=0)
            tournament_creator_data = StringVar(value=data[i][4])
            tournament_creator = customtkinter.CTkLabel(
                div, textvariable=tournament_creator_data)
            tournament_creator.grid(row=3, column=1)
            #! Tournament Type
            tournament_type_label = customtkinter.CTkLabel(
                div, text="Tournament's Type")
            tournament_type_label.grid(row=4, column=0)
            tournament_type_data = StringVar(value=data[i][5])
            tournament_type = customtkinter.CTkLabel(
                div, textvariable=tournament_type_data)
            tournament_type.grid(row=4, column=1)
            #! Actions
            action_label = customtkinter.CTkLabel(div, text="Actions :")
            action_label.grid(row=5, column=0)
            actions = customtkinter.CTkFrame(div, height=30)
            actions.grid(row=5, column=1)
            removeBtn = customtkinter.CTkButton(actions, text="Remove",command= lambda idtournament=data[i][0] : removeTournament(idtournament,root))
            removeBtn.grid(row=0, column=0)
            # updateBtn = customtkinter.CTkButton(actions, text="Edit")
            idtournament = tournament_title_data.get()

            # updateBtn = customtkinter.CTkButton(
            #     actions, text="Update", command=lambda idtournament=data[i][0]: updateTournament(idtournament, root))
            optionSelected = StringVar()
            updateBtn = customtkinter.CTkOptionMenu(actions,values=["Players","Edit Tournament","Matches"],command= lambda  choice = optionSelected ,id = data[i][0]: optionMenu(choice,id,root),variable=optionSelected)
            updateBtn.set("Update")
            # print(idtournament)
            updateBtn.grid(row=0, column=1)


def getTournamentData():
    connect = sqlite3.connect("./database/database.db")
    cursor = connect.cursor()
    data = cursor.execute("SELECT * FROM tournament").fetchall()
    connect.commit()
    connect.close()
    return data

def getSpecificTournament(idTournament):
    connect = sqlite3.connect("./database/database.db")
    cursor= connect.cursor()
    tournament =cursor.execute(f"SELECT * FROM tournament where id = ?",(idTournament,)).fetchone()
    connect.commit()
    connect.close()
    return tournament

def updateTournament(idTournament,root):
    data = getSpecificTournament(idTournament)
    # print(data)
    window = customtkinter.CTkToplevel(root)
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
    type = customtkinter.CTkOptionMenu(input_frame, values=["LOCAL", "REGIONAL"])
    place = customtkinter.CTkEntry(input_frame, placeholder_text="place")
    date = customtkinter.CTkEntry(input_frame, placeholder_text="date")
    btn1 = customtkinter.CTkButton(input_frame, text="update", command=lambda id=idTournament,fullname = fullName,title=title,type=type,place=place,date=date: updateInfos(id,fullname,title,type,place,date))

    fullName.insert(customtkinter.END,data[4])
    title.insert(customtkinter.END,data[1])
    type.set(data[5])
    place.insert(customtkinter.END,data[2])
    date.insert(customtkinter.END,data[3])
    # 
    fullName.pack(pady=5, expand=True)
    title.pack(pady=5, expand=True)
    type.pack(pady=5, expand=True)
    place.pack(pady=5, expand=True)
    date.pack(pady=5, expand=True)
    btn1.pack(pady=5, expand=True)


def updateInfos(id,fullname,title,type,place,date):
    fulnameNew = fullname.get()
    titleNew = title.get()
    typeNew = type.get()
    placeNew = place.get()
    dateNew = date.get()
    try:
        connect = sqlite3.connect("./database/database.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE tournament SET title = ? , place = ? , date = ? , name_of_creator = ? , type = ? WHERE id = ? ",(titleNew,placeNew,dateNew,fulnameNew,typeNew,id))
        connect.commit()
        connect.close()
    except:
        print("error")
    
def removeTournament(id,root):
    try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("DELETE FROM  tournament WHERE id = ? ",(id,))
            
            connect.commit()
            connect.close()
            
            MessageBox(root,"The Tournament is Deleted","success")
    except:
            MessageBox(root,"Failed to delete the tournament","error")
def optionMenu(choice,id,root):
    if(choice == "Edit Tournament"):
        updateTournament(id,root)
    # print(f"choice : {choice}")
    # print(f"id {id}")