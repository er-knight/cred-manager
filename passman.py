import sqlite3

class passman:

    def __init__(self):

        connection = sqlite3.connect("passwords.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (website TEXT, username TEXT, password TEXT)""")

    def insert_password(self, website, username, password):

        connection = sqlite3.connect("passwords.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""SELECT * FROM passwords WHERE website=? AND username=? AND password=?""", 
                (website, username, password))

            passwords = db_cursor.fetchall()

            if passwords:
                return "username and password already exists\ndo you want to update it?"

            db_cursor.execute("""INSERT INTO passwords VALUES (?, ?, ?)""", 
                (website, username, password))

            return "username and password added successfully!"

    def search_password(self, website):
        # TODO 
        # search passwords for given websites
        # if one or more entries found, print them
        # else print proper message
        ...

    def update_username(self, website, password=None):
        # TODO
        # search username for given website
        # if there are multiple entries, print all of them
        # and ask users for password for which they want update username
        # if there is one entry, ask for conformation and update username
        # if none, return proper message
        ...

    def update_password(self, website, username=None):
        # TODO
        # search passwords for given websites
        # if there are multiple entries, print all of them
        # and ask users for username for which they want update password
        # if there is one entry, ask for conformation and update password
        # if none, return proper message
        ...
        
    
    def delete_password(self, website, username=None):
        # TODO
        # search passwords for given websites
        # if there are multiple entries, print all of them
        # and ask users for username for which they want delete password
        # if there is one entry, ask for conformation and delete password
        # if none, return proper message
        ...

if __name__ == "__main__":

    passwordmanager = passman()

    # TODO : tests