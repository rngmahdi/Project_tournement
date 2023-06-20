import customtkinter 
import sqlite3
from tkinter import ttk
import tkinter as tk
from PIL import Image
from message_box import MessageBox

class PlayerPage(customtkinter.CTk):
    def __init__(self,container):
        super().__init__()
        
        self.main = container
        # Main
        
        self.addPlayer_frame = customtkinter.CTkFrame(self.main,width=600,)
        self.addPlayer_frame.columnconfigure((0,1),weight=1)
        self.addPlayer_frame.rowconfigure(0,weight=1)
        self.addPlayer_frame.grid(column=0,sticky="news")
        self.listPlayer_frame = customtkinter.CTkScrollableFrame(self.main,width=600,)
        self.listPlayer_frame.grid(column=0)
        
        self.form_frame = customtkinter.CTkFrame(self.addPlayer_frame)
        self.form_frame.grid(row=0,column=1,sticky="news")
        self.fullName = customtkinter.CTkEntry(self.form_frame,placeholder_text="fullName")
        self.fullName.pack(pady=5,expand=True)
        self.rating = customtkinter.CTkEntry(self.form_frame,placeholder_text="rating")
        self.rating.pack(pady=5,expand=True)
        self.phone = customtkinter.CTkEntry(self.form_frame,placeholder_text="phone")
        self.phone.pack(pady=5,expand=True)
        self.email = customtkinter.CTkEntry(self.form_frame,placeholder_text="email")
        self.email.pack(pady=5,expand=True)
        self.btn1 = customtkinter.CTkButton(self.form_frame,text="Add PLayer",command=self.addPlayer)
        self.btn1.pack(pady=5,expand=True)
        
        self.form_img = customtkinter.CTkFrame(self.addPlayer_frame)
        self.form_img.grid(row=0,column=0,sticky="news")
        
        self.img = customtkinter.CTkImage(dark_image=Image.open("./public/img/pbg.png"),size=(300,250))
        
        self.img_bg = customtkinter.CTkLabel(self.form_img,image=self.img,text="")
        self.img_bg.grid(row=0,column=1,sticky="news")
        
        self.getAllPlayers()
        
        
    def addPlayer(self):
        try:
            fullName = self.fullName.get()
            phone = self.phone.get()
            email = self.email.get()
            rating = self.rating.get()
            if(fullName == "" or phone == "" or email == "" or rating == ""):
                MessageBox(self.main,"Not a Valid Player","warning")
            else:
                connect = sqlite3.connect("./database/database.db")
                cursor = connect.cursor()

                cursor.execute("INSERT INTO player (fullname,rating,phone,email) VALUES (?,?,?,?)",(fullName,rating,phone,email))
                connect.commit()
                connect.close()
                self.getAllPlayers()
                self.clearForm()
                MessageBox(self.main,"The Player is Added","success")
                
        except:
            MessageBox(self.main,"Failed to add the Player","error")
            
    def deletePlayer(self,id):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            cursor.execute("DELETE FROM  player WHERE id = ? ",(id,))
            
            connect.commit()
            connect.close()
            self.getAllPlayers()
            MessageBox(self.main,"The Player is Deleted","success")
        except:
            MessageBox(self.main,"Failed to delete the Player","error")
            
    def getAllPlayers(self):
        try:
            connect = sqlite3.connect("./database/database.db")
            cursor = connect.cursor()

            data = cursor.execute("SELECT * FROM player").fetchall()
            connect.commit()
            connect.close()
            
            self.cleanContainer(self.listPlayer_frame)
            self.listPlayer_frame.columnconfigure(0,weight=1)
            
            for i in range(0,len(data)):
                div = customtkinter.CTkFrame(self.listPlayer_frame,height=70)
                div.grid(row=i,column=0,sticky="ew",pady=5)
                div.columnconfigure(0,weight=6)
                div.columnconfigure((1,2),weight=1)
                
                customtkinter.CTkLabel(div,text=(data[i][1]).upper()).grid(row=i,column=0,sticky="w",pady=10,padx=5)
                customtkinter.CTkButton(div,text="Edit",command=lambda id=data[i][0]:self.editPlayer(id)).grid(row=i,column=1,sticky="e")            
                customtkinter.CTkButton(div,text="Remove",command=lambda id=data[i][0]:self.deletePlayer(id)).grid(row=i,column=2,sticky="e") 
                
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
            self.getAllPlayers()
            MessageBox(self.main,"The Player is Updated","success")
            
        except:
            MessageBox(self.main,"Failed to Update The Player","error")
    
    def clearForm(self):
        self.fullName.delete(0,customtkinter.END)
        self.rating.delete(0,customtkinter.END)
        self.phone.delete(0,customtkinter.END)
        self.email.delete(0,customtkinter.END)
        
    def cleanContainer(self,container):
        for widget in container.winfo_children(): 
            widget.destroy()