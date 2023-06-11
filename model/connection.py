from tkinter import *
import mysql.connector

def Connection():
   try:
      connect = mysql.connector.connect(host = "localhost",
                                       user = "root",
                                       password = "",
                                       db = "dbtournament")
      return connect
   except:
      print("Couldn't connect to database")







