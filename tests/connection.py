import sqlite3

connect = sqlite3.connect("./database/database.db")
cursor = connect.cursor()

cursor.execute("SELECT * FROM player")
print(cursor.fetchall())
connect.commit()
connect.close()