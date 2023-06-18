import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk


class PlayerPage(customtkinter.CTk):
    def __init__(self,container):
        super().__init__()
        
        self.main = container
        # Main
        
        self.addPlayer_frame = customtkinter.CTkFrame(self.main,width=600)
        self.addPlayer_frame.grid(column=0,sticky="news")
        self.listPlayer_frame = customtkinter.CTkScrollableFrame(self.main,width=600)
        self.listPlayer_frame.grid(column=0,sticky="news")
        
        self.fullName = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="fullName")
        self.fullName.grid()
        self.rating = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="rating")
        self.rating.grid()
        self.phone = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="phone")
        self.phone.grid()
        self.email = customtkinter.CTkEntry(self.addPlayer_frame,placeholder_text="email")
        self.email.grid()
        self.btn1 = customtkinter.CTkButton(self.addPlayer_frame,text="Add PLayer",command=self.addPlayer)
        self.btn1.grid(pady=10)
        
        players = self.getAllPlayers()
        for i in range(0,len(players)):
            customtkinter.CTkLabel(self.listPlayer_frame,text=players[i][1]).grid(row=i,column=1)
            customtkinter.CTkButton(self.listPlayer_frame,text="Edit",command=lambda id=players[i][0]:self.editPlayer(id)).grid(row=i,column=2)            
            customtkinter.CTkButton(self.listPlayer_frame,text="Remove",command=lambda id=players[i][0]:self.deletePlayer(id)).grid(row=i,column=3) 
        

    def test(self,id):
        print(id)
    
    def addPlayer(self):
        try:
            fullName = self.fullName.get()
            phone = self.phone.get()
            email = self.email.get()
            rating = self.rating.get()
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("INSERT INTO player (fullname,rating,phone,email) VALUES (?,?,?,?)",(fullName,phone,email,rating))
            connect.commit()
            connect.close()
            print("Player Addes")
        except:
            print("Failed to Add Player")
            
    def deletePlayer(self,id):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("DELETE FROM  player WHERE id = ? ",(id,))
            
            connect.commit()
            connect.close()
            print("Player is deleted")
        except:
            print("Failed to delete player")
            
    def getAllPlayers(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            data = cursor.execute("SELECT * FROM player").fetchall()
            connect.commit()
            connect.close()
            return data
        except:
            return False
    
    def getOnePlayer(self,id):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            data = cursor.execute("SELECT * FROM player WHERE id = ?",(id,)).fetchone()
            connect.commit()
            connect.close()
            return data
        except:
            return False
    
    def editPlayer(self,id):
        player = self.getOnePlayer(id)
        print(player)
        
        self.clearForm()
        self.fullName.insert(customtkinter.END,player[1])
        self.rating.insert(customtkinter.END,player[2])
        self.phone.insert(customtkinter.END,player[3])
        self.email.insert(customtkinter.END,player[4])
        
        
        self.btn1.configure(text="Update",command=lambda id=player[0]:self.updatePlayer(id))
        
        
    def updatePlayer(self,id):
        
        fullName = self.fullName.get()
        phone = self.phone.get()
        email = self.email.get()
        rating = self.rating.get()
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            data = cursor.execute("UPDATE player SET fullName = ? , rating = ? , phone = ? , email = ? WHERE id = ?;",(fullName,rating,phone,email,id))
            connect.commit()
            connect.close()
            self.btn1.configure(text="Add Player",command=self.addPlayer)
            self.clearForm()
            print("player is updated")
        except:
            print("failed to update")
    
    def clearForm(self):
        self.fullName.delete(0,customtkinter.END)
        self.rating.delete(0,customtkinter.END)
        self.phone.delete(0,customtkinter.END)
        self.email.delete(0,customtkinter.END)