import mysql.connector
from mysql.connector import errorcode


class MySQLConnection:
    def __init__(self, *, host, database, user, password):
        self.cnx = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)
        self.cursor = self.cnx.cursor()

    def __del__(self):
        self.cursor.close()
        self.cnx.close()

    def get(self, command):
        try:
            self.cursor.execute(command)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("get: OK")

        return(list(self.cursor))

    def execute(self, command):
        try:
            self.cursor.execute(command)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("execute: OK")

        self.cnx.commit()

    def insert_values(self, insert_command, value_list):
        for value in value_list:
            self.cursor.execute(insert_command, value)
        self.cnx.commit()
