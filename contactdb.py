import sqlite3

class Contact:
    def __init__(self,contact):
        #,name,email,address,phone_no,_id
        _id,name,phone_no,email,address = contact
        self.name = name
        self.email = email
        self.address = address
        self.phone_no = phone_no
        self.id = _id
    """
    @staticmethod
    def deserialize(self,contact):
        return
    """
    def __str__(self) -> str:
        return self.name
    


class ContactBook:
    def __init__(self):
        self.conn = sqlite3.connect('contactBook.db')
        self.cursor = self.conn.cursor()
        createTableCmd = "CREATE TABLE IF NOT EXISTS Contacts(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100),phone_no VARCHAR(50), email VARCHAR(255), address VARCHAR(255))"
        self.cursor.execute(createTableCmd)


    def addContact(self,name,phone_no,email,address):
        addCmd = "INSERT INTO Contacts(name, phone_no, email, address) VALUES(?,?,?,?)"
        self.cursor.execute(addCmd,(name,phone_no,email,address))
        self.conn.commit()
    
    def getContact(self,id):
        q = "SELECT * FROM Contacts WHERE id = ?"

        return self.cursor.execute(q,(id,)).fetchone()

    def searchContact(self,query=''):
        searchQuery = "SELECT * FROM Contacts WHERE UPPER(name) LIKE ?"
        query = f"%{ query.upper() }%"
        self.cursor.execute(searchQuery,(query,))
        for c in self.cursor.fetchall():
            C = Contact(c)
            yield C
    def updateContact(self,id,**kwargs):
        cmd = "UPDATE Contacts SET "
        cc = []
        for k,v in kwargs.items():
            cc.append(k+" = "+'?')
        cc = ",".join(cc)
        cmd+= cc+" WHERE id = ?"
        tt = tuple(kwargs.values())+(id,)
        self.cursor.execute(cmd,tt)
        self.conn.commit()

    def deleteContact(self,id):
        delQuery = "DELETE FROM Contacts WHERE id = ?"
        self.cursor.execute(delQuery,(id,))
        self.conn.commit()

        








    
        