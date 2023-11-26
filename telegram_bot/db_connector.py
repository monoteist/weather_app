import os

import psycopg2

DATABASE = os.getenv('DATABASE')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

class DatabaseConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password,
                                              host=self.host, port=self.port)
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

db_connector = DatabaseConnector(dbname=DATABASE, user=POSTGRES_USER,
                                 password=POSTGRES_PASSWORD, host=HOST, port=PORT)

def execute_query(query, fetch_all=True):
    connection = db_connector.connect()
    cursor = connection.cursor()
    cursor.execute(query)
    
    if fetch_all:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()

    cursor.close()
    db_connector.disconnect()

    return result


