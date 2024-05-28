import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Baglandi")
            return self.connection
        except mysql.connector.Error as err:
            print(err)
            return False

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Veri tabanı bağlantısı kapatıldı.")
