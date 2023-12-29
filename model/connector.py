import sqlite3

class Connector():
    def __init__(self):
        self.connect = sqlite3.connect("../database/database.db")
        self.cursor = self.connect.cursor()
        
        
 