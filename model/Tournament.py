import connector

class Tournament:
    def __init__(self, owner, title, type, place, date):
        self.owner = owner
        self.title = title
        self.type = type
        self.place = place
        self.date = date

    def create(self):
        try:

            db = connector.Connector()
            db.cursor.execute("INSERT INTO tournament (title,place,date,name_of_creator,type) VALUES (?,?,?,?,?)",(self.title, self.place, self.date, self.owner, self.type))
            db.connect.commit()
            db.connect.close()
            
        except:
            return -1

    def read(id):
        try:
            db = connector.Connector()

            data = db.cursor.execute("SELECT * FROM tournament WHERE id = ?",(id)).fetchone()
            db.connect.commit()
            db.connect.close()
            
            return data
        except:
            return -1

    def update(self,id):
        try:
            db = connector.Connector()

            db.cursor.execute("UPDATE tournament SET title = ? , place = ? , name_of_creator = ? WHERE id = ?;",(self.title, self.place, self.owner,id))
            db.connect.commit()
            db.connect.close()

        except:
            return -1

    def delete(self,id):
        try:
            db = connector.Connector()
            db.cursor.execute("DELETE FROM  tournament WHERE id = ? ", (id))

            db.connect.commit()
            db.connect.close()
            
            return id

        except:
            return -1