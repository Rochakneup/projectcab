import mysql.connector
import sys
class Connect:
    __connection = None
    __cursor = None

    def __init__(self):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.password = ''
        self.database = 'taxi'
        self.connectdatabase()

    def connectdatabase(self):
        try:
            if not Connect.__connection:
                Connect.__connection = mysql.connector.connect(host=self.host,
                                                               port=self.port,
                                                               user=self.user,
                                                               password=self.password,
                                                               database=self.database)
                Connect.__cursor = Connect.__connection.cursor()
                Connect.__connection.autocommit = True
        except:
            print("Error", sys.exc_info())

    @property
    def cursor(self):
        return Connect.__cursor