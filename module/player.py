import tkinter as tk
import customtkinter 
import sqlite3


class Player(customtkinter.CTk):
    def __init__(self,window):
        super().__init__()
        
        # Main
        for child in window.winfo_children():
            child.destroy()
        
        print("called")
            
        # window.title("PLayers Section")

        
        
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
    