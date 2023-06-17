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
        
        
        self.tree = ttk.Treeview(self.listPlayer_frame, columns=('id','fullName', 'rating','phone' ,'email','tournamentId'), show='headings')
        self.tree.pack()
        self.tree.heading('id', text='id')
        self.tree.heading('fullName', text='Full Name')
        self.tree.heading('rating', text='Rating')
        self.tree.heading('phone', text='Phone')
        self.tree.heading('email', text='Email')
        self.tree.heading('tournamentId', text='Tour Id')

        self.tree.column('id', anchor=tk.CENTER, width=80)
        self.tree.column('fullName', anchor=tk.CENTER, width=80)
        self.tree.column('rating', anchor=tk.CENTER, width=80)
        self.tree.column('phone', anchor=tk.CENTER, width=80)
        self.tree.column('email', anchor=tk.CENTER, width=80)
        self.tree.column('tournamentId', anchor=tk.CENTER, width=80)
        
        # print(self.getAllPlayers())
        for elem in self.getAllPlayers():
            self.tree.insert('', tk.END, values=elem)
        
        
        self.tree.bind("<<TreeviewSelect>>", self.playerOps)

    def playerOps(self,a):
        frame = customtkinter.CTkFrame(self.addPlayer_frame)
        
        selectedItem = self.tree.selection()[0]
        print(self.tree.item(selectedItem))
        self.btn1.destroy()
        self.btn1 = customtkinter.CTkButton(frame,text="Update PLayer")
        self.btn1.grid(row=5,column=1)
        self.btn1 = customtkinter.CTkButton(frame,text="Remove PLayer")
        self.btn1.grid(row=5,column=2)
        
        frame.grid()
    
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
        
    def updatePlayer(self):
        pass