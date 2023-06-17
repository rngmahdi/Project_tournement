from tkinter import *
from tkinter import ttk
import customtkinter
import sqlite3


def TournamentList(root):
    frame = customtkinter.CTkFrame(root)
    frame.pack()

    data = getTournamentData()
    if (len(data) != 0):
        for i in range(len(data)):
            pass
            #   print(data)
            div = customtkinter.CTkFrame(frame)
            div.pack(padx=10, pady=10)
            #! tournament title 
            tournament_title_label = customtkinter.CTkLabel(div, text="Tournament's title :")
            tournament_title_label.grid(row=0, column=0)
            tournament_title_data = StringVar(value=data[i][1])
            tournament_title = customtkinter.CTkLabel(div, textvariable=tournament_title_data)
            tournament_title.grid(row=0, column=1, padx=20)
            #! tournament's place 
            tournament_place_label= customtkinter.CTkLabel(div,text="Place :")
            tournament_place_label.grid(row=1,column=0)
            tournament_place_data = StringVar(value=data[i][2])
            tournament_place= customtkinter.CTkLabel(div,textvariable=tournament_place_data)
            tournament_place.grid(row=1,column=1)
            #! Tournament Date
            tournament_date_label = customtkinter.CTkLabel(div,text="Date")
            tournament_date_label.grid(row=2,column=0)
            tournament_date_data = StringVar(value=data[i][3])
            tournament_date = customtkinter.CTkLabel(div,textvariable=tournament_date_data)
            tournament_date.grid(row=2,column=1)
            #! tournament creator's Name
            tournament_creator_label = customtkinter.CTkLabel(div,text="Creator")
            tournament_creator_label.grid(row=3,column=0)
            tournament_creator_data = StringVar(value=data[i][4])
            tournament_creator = customtkinter.CTkLabel(div,textvariable=tournament_creator_data)
            tournament_creator.grid(row=3,column=1)
            #! Tournament Type 
            tournament_type_label = customtkinter.CTkLabel(div,text="Tournament's Type")
            tournament_type_label.grid(row=4,column=0)
            tournament_type_data = StringVar(value=data[i][5])
            tournament_type = customtkinter.CTkLabel(div,textvariable=tournament_type_data)
            tournament_type.grid(row=4,column=1) 
            #! Actions 
            action_label = customtkinter.CTkLabel(div,text="Actions :")
            action_label.grid(row=5,column=0)
            actions= customtkinter.CTkFrame(div,height=30)
            actions.grid(row=5,column=1)
            removeBtn = customtkinter.CTkButton(actions,text="Remove")
            removeBtn.grid(row=0,column=0)
            updateBtn = customtkinter.CTkButton(actions,text="Edit")
            updateBtn = customtkinter.CTkButton(actions,text="Update",command=lambda : print(i))
            updateBtn.grid(row=0,column=1)


def getTournamentData():
    connect = sqlite3.connect("./database/database.db")
    cursor = connect.cursor()
    data = cursor.execute("SELECT * FROM tournament").fetchall()
    connect.commit()
    connect.close()
    return data
