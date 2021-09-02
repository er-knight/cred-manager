import sqlite3

class manager:

    def __init__(self):

        connection = sqlite3.connect("credentials.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""CREATE TABLE IF NOT EXISTS credentials (website TEXT, username TEXT, password TEXT)""")

    def insert(self, website, username, password):

        connection = sqlite3.connect("credentials.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""SELECT * FROM credentials WHERE website=? AND username=? AND password=?""", 
                (website, username, password))

            credentials = db_cursor.fetchall()

            if credentials:
                return "username and password already exists\ndo you want to update it?"

            db_cursor.execute("""INSERT INTO credentials VALUES (?, ?, ?)""", (website, username, password))

            return "username and password added successfully!"

    def search(self, website):

        connection = sqlite3.connect("credentials.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""SELECT * FROM credentials WHERE website=?""", (website, ))

            credentials = db_cursor.fetchall()

            if not credentials:
                return f"no data found for {website}"

            return credentials

    def update(self, website=None, username=None, oldusername=None, oldpassword=None, password=None):
        # https://www.sqlitetutorial.net/sqlite-replace-statement/
        # TODO
        # search username for given website
        # if there are multiple entries, print all of them
        # and ask users for password for which they want update username
        # if there is one entry, ask for conformation and update username
        # if none, return proper message
        # TODO
        # search credentials for given websites
        # if there are multiple entries, print all of them
        # and ask users for username for which they want update password
        # if there is one entry, ask for conformation and update password
        # if none, return proper message
        ...
    
    def delete(self, website, username, password=None):

        connection = sqlite3.connect("credentials.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""DELETE FROM credentials WHERE website=? AND username=?""", (website, username))


        # TODO
        # search credentials for given websites
        # if there are multiple entries, print all of them
        # and ask users for username for which they want delete password
        # if there is one entry, ask for conformation and delete password
        # if none, return proper message
        ...

    # TODO:
    # count total credential entries
    # https://www.sqlitetutorial.net/sqlite-count-function/

if __name__ == "__main__":

    ...

    # TODO : tests