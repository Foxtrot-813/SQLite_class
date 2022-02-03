import sqlite3


class Database:

    def __init__(self, filename):
        self.__connect__ = sqlite3.connect(filename)
        self.__cursor___ = self.__connect__.cursor()

    # This is just a Decorator instead of using self.__connect__ in future methods we can just use self.connection.
    @property
    def connection(self):
        return self.__connect__

    # This is just a Decorator instead of using self.__cursor___ in future methods we can just use self.cursor.
    @property
    def cursor(self):
        return self.__cursor___

    # This method is just to save what we have done.
    def commit(self):
        return self.connection.commit()

    # This method is to close the database connection.
    def close(self):
        return self.cursor.close()

    # This method is for executing statements
    def execute(self, ):
        self.cursor.execute(statement)
        return

    # This method is for printing info, same like execute method but this on is for printing info only.
    def get_info(self, results):
        for row in self.cursor.execute(results):
            print(row)

    # This method will get all information we have about a table
    def fetchall(self, table):
        for row in self.cursor.execute(table).fetchall():
            print(row)

    # This method will get only the first row information we have about a table
    def fetchone(self, table):
        print(self.cursor.execute(table).fetchone())


db = Database('Your file name')
sql = '''SELECT * 
         FROM table 
         WHERE Lastname = 'name';'''

statement = '''INSERT INTO table (FirstName, LastName)
      VALUES ('fname', 'lname')'''

db.execute(q)
db.fetchall(sql)
