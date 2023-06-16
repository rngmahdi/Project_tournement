import tkinter as tk
import customtkinter 
import sqlite3


class Player(customtkinter.CTk):
    def __init__(self,window):
        super().__init__()
        
        # Main
        self.window = window
        for child in self.window.winfo_children():
            child.destroy()
            
        self.window.title("PLayers Section")
        
        self.frame_1 = customtkinter.CTkFrame(window,height=100,width=200)
        self.fullName = customtkinter.CTkEntry(self.frame_1,placeholder_text="fullName")
        self.rating = customtkinter.CTkEntry(self.frame_1,placeholder_text="rating")
        self.phone = customtkinter.CTkEntry(self.frame_1,placeholder_text="phone")
        self.email = customtkinter.CTkEntry(self.frame_1,placeholder_text="email")
        
        self.frame_2 = customtkinter.CTkFrame(window,height=100,width=200)
        self.btn1 = customtkinter.CTkButton(self.frame_2,text="Add PLayer")
        self.btn2 = customtkinter.CTkButton(self.frame_2,text="Cancel")
        
        self.frame_3 = customtkinter.CTkFrame(self.window,height=100,width=200)
        self.getPlayers()
        
        
        
        self.frame_1.grid()
        self.fullName.grid()
        self.rating.grid()
        self.phone.grid()
        self.email.grid()
        
        
        self.frame_2.grid()
        self.btn1.grid()
        self.btn2.grid()
        
        self.frame_3.grid()
            

    def getPlayers(self):
        connect = sqlite3.connect("./database/database.db")
        cursor = connect.cursor()

        data = cursor.execute("SELECT * FROM player").fetchall()
        connect.commit()
        connect.close()
        print(data)
        

    # Methods
    # def add(self):
        
    #     fullName = self.fullName.get()
    #     title = self.title.get()
    #     type = self.type.get()
    #     place = self.place.get()
    #     date = self.date.get()
        

    #     connect = sqlite3.connect("./database/database.db")
    #     cursor = connect.cursor()

    #     cursor.execute("INSERT INTO dbtournament (title,place,date,name_of_creator,type) VALUES (?,?,?,?,?)",(title,place,date,fullName,type))
    #     connect.commit()
    #     connect.close()
    