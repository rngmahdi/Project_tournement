import sqlite3

connect = sqlite3.connect("./database/database.db")
cursor = connect.cursor()

print(cursor.execute("SELECT * FROM player").fetchall())
connect.commit()
connect.close()